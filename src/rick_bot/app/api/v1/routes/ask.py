
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services.user_service import UserService
from app.dependencies import get_db
from app.core.security import get_current_user



router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/ask", response_model=AgentAskResponse)
def ask(
    body: GenericAskRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = AgentService(db)
    return service.orchestrate(body, user=current_user)

@router.post("/ask/{agent_id}", response_model=AgentAskResponse)
def ask_specific_agent(
    agent_id: UUID,
    body: DirectAskRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    service = AgentService(db)
    return service.ask_specific_agent(agent_id, body, user=current_user)

@router.post("/ask/teams", response_model=AgentAskResponse)
def ask_by_teams(
    body: GenericAskRequest,
    db: Session = Depends(get_db),
    auth_header: str = Header(None)
):
    service = AgentService(db)
    integration = AppIntegrationService(db).validate_integration(auth_header)
    return service.orchestrate(body, integration=integration)
