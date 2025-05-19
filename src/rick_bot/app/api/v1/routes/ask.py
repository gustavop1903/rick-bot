
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserUpdate
from app.services.user_service import UserService
from app.dependencies import get_db
from app.core.security import get_current_user



router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/ask", response_model=AgentAskResponse)
def ask_generic(body: GenericAskRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return AskService(db).handle(question=body.question, user=user)

@router.post("/ask/{agent_id}", response_model=AgentAskResponse)
def ask_specific(agent_id: str, body: DirectAskRequest, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return AskService(db).handle(question=body.question, user=user, agent_id=agent_id)

@router.post("/ask/team", response_model=AgentAskResponse)
def ask_team(body: GenericAskRequest, db: Session = Depends(get_db), request: Request = None):
    integration = AppIntegrationService(db).validate_teams_request(request)
    return AskService(db).handle(question=body.question, integration=integration)
