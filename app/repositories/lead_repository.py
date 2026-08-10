from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.lead import Lead


class LeadRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Lead).all()

    def get_by_id(self, lead_id: int):
        return (
            self.db.query(Lead)
            .filter(Lead.id == lead_id)
            .first()
        )

    def create(self, lead_data: dict):
        lead = Lead(**lead_data)

        self.db.add(lead)
        self.db.commit()
        self.db.refresh(lead)

        return lead

    def update(self, lead_id: int, data: dict):
        lead = self.get_by_id(lead_id)

        if not lead:
            return None

        for key, value in data.items():
            setattr(lead, key, value)

        self.db.commit()
        self.db.refresh(lead)

        return lead

    def delete(self, lead_id: int):
        lead = self.get_by_id(lead_id)

        if not lead:
            return False

        self.db.delete(lead)
        self.db.commit()

        return True

    def list_leads(
        self,
        search: str | None = None,
        status: str | None = None,
        property_type: str | None = None,
        source: str | None = None,
        page: int = 1,
        page_size: int = 10,
    ):

        query = self.db.query(Lead)

        # Search
        if search:
            search = search.lower()

            query = query.filter(
                or_(
                    Lead.name.ilike(f"%{search}%"),
                    Lead.phone.ilike(f"%{search}%"),
                    Lead.email.ilike(f"%{search}%"),
                )
            )

        # Status
        if status:
            query = query.filter(
                Lead.status == status
            )

        # Property type
        if property_type:
            query = query.filter(
                Lead.property_type == property_type
            )

        # Source
        if source:
            query = query.filter(
                Lead.source == source
            )

        total = query.count()

        start = (page - 1) * page_size

        items = (
            query
            .offset(start)
            .limit(page_size)
            .all()
        )

        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "items": items,
        }