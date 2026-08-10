from datetime import datetime
from sqlalchemy.orm import Session

from app.repositories.lead_repository import LeadRepository


class LeadService:

    def __init__(self, db: Session):
        self.repository = LeadRepository(db)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, lead_id: int):
        return self.repository.get_by_id(lead_id)

    def create(self, lead_data: dict):

        lead_data["status"] = "new"
        lead_data["created_at"] = datetime.now()
        lead_data["updated_at"] = datetime.now()

        return self.repository.create(lead_data)

    def update(self, lead_id: int, data: dict):

        data["updated_at"] = datetime.now()

        return self.repository.update(
            lead_id,
            data
        )

    def delete(self, lead_id: int):

        return self.repository.delete(lead_id)

    def list_leads(
        self,
        search=None,
        status=None,
        property_type=None,
        source=None,
        page=1,
        page_size=10,
    ):

        return self.repository.list_leads(
            search=search,
            status=status,
            property_type=property_type,
            source=source,
            page=page,
            page_size=page_size,
        )