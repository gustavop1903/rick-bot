from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from ..domain.schemas import AgentCreate, AgentOut, AgentUpdate, UserOut
from ..services import AgentService
from ....config.security.security import get_db, get_current_user

agent = APIRouter(prefix="/agents", tags=["Agents"])

@agent.post("/", response_model=AgentOut)
def create_agent(
    data: AgentCreate,
    db: Session = Depends(get_db),
    current_user: UserOut = Depends(get_current_user)
):
    return AgentService(db).create_agent(data, current_user.id)

@agent.get("/", response_model=list[AgentOut])
def list_agents(db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    return AgentService(db).list_agents_by_user(current_user.id)

@agent.get("/{agent_id}", response_model=AgentOut)
def retrieve_agent(agent_id: UUID, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    agent = AgentService(db).get_agent_by_id(agent_id)
    if not agent or agent.creator_id != current_user.id:
        raise HTTPException(status_code=404, detail="Agente não encontrado")
    return agent

@agent.put("/{agent_id}", response_model=AgentOut)
def update_agent(agent_id: UUID, data: AgentUpdate, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    return AgentService(db).update_agent(agent_id, data, current_user.id)

@agent.delete("/{agent_id}", status_code=204)
def delete_agent(agent_id: UUID, db: Session = Depends(get_db), current_user: UserOut = Depends(get_current_user)):
    AgentService(db).delete_agent(agent_id, current_user.id)
