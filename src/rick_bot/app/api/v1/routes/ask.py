
from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session

from domain.schemas import AgentAskResponse, GenericAskRequest, DirectAskRequest
from domain.models import User
from ..services import AskService, AppIntegrationService   
from ....config.security.security import get_db
from app.config.security.security import get_current_user



ask = APIRouter(prefix="/users", tags=["Users"])

@ask.post("/ask", response_model=AgentAskResponse)
def ask_generic(body: GenericAskRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return AskService(db).handle(question=body.question)

@ask.post("/ask/{agent_id}", response_model=AgentAskResponse)
def ask_specific(agent_id: str, body: DirectAskRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return AskService(db).handle(question=body.question, agent_id=agent_id)

#@ask.post("/ask/teams", response_model=AgentAskResponse)
def ask_teams(body: GenericAskRequest, db: Session = Depends(get_db), request: Request = None):
    integration_data = AppIntegrationService(db).validate_teams_request(request)
    session_id = f"{integration_data['from']['id']}_{integration_data['conversation']['tenantId']}"
    
    return AskService(db).handle(
        question=body.question,
        session_id=session_id
    )
