
from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Any
from datetime import datetime

class QuestionRequest(BaseModel):
  question: str