from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.lead import LeadCreate, LeadUpdate
from app.services.lead_service import LeadService
from app.dependencies.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/leads",
    tags=["Leads"]
)


@router.get("/")
def get_all(
    search: str | None = Query(default=None),
    status: str | None = Query(default=None),
    property_type: str | None = Query(default=None),
    source: str | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LeadService(db)

    return service.list_leads(
        search=search,
        status=status,
        property_type=property_type,
        source=source,
        page=page,
        page_size=page_size,
    )

@router.get("/{lead_id}")
def get_one(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LeadService(db)

    return service.get_by_id(lead_id)


@router.post("/")
def create(
    lead: LeadCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LeadService(db)

    return service.create(
        lead.model_dump()
    )


@router.patch("/{lead_id}")
def update(
    lead_id: int,
    lead: LeadUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LeadService(db)

    return service.update(
        lead_id,
        lead.model_dump(exclude_unset=True)
    )


@router.delete("/{lead_id}")
def delete(
    lead_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    service = LeadService(db)

    service.delete(lead_id)

    return {
        "message": "Deleted Successfully"
    }