from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database.database import get_db
from app.models.lead import Lead

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):
    total_leads = db.query(Lead).count()

    new_leads = (
        db.query(Lead)
        .filter(Lead.status == "new")
        .count()
    )

    contacted_leads = (
        db.query(Lead)
        .filter(Lead.status == "contacted")
        .count()
    )

    converted_leads = (
        db.query(Lead)
        .filter(Lead.status == "converted")
        .count()
    )

    lost_leads = (
        db.query(Lead)
        .filter(Lead.status == "lost")
        .count()
    )

    total_budget = (
        db.query(func.coalesce(func.sum(Lead.budget), 0))
        .scalar()
    )

    conversion_rate = (
        (converted_leads / total_leads) * 100
        if total_leads > 0
        else 0
    )

    return {
        "total_leads": total_leads,
        "new_leads": new_leads,
        "contacted_leads": contacted_leads,
        "converted_leads": converted_leads,
        "lost_leads": lost_leads,
        "total_budget": total_budget,
        "conversion_rate": round(conversion_rate, 2)
    }