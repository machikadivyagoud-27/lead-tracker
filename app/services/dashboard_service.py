from app.storage.memory import leads


class DashboardService:

    def get_dashboard(self):

        all_leads = list(leads.values())

        total_leads = len(all_leads)

        new_leads = len(
            [lead for lead in all_leads if lead["status"] == "new"]
        )

        contacted_leads = len(
            [lead for lead in all_leads if lead["status"] == "contacted"]
        )

        closed_leads = len(
            [lead for lead in all_leads if lead["status"] == "closed"]
        )

        lost_leads = len(
            [lead for lead in all_leads if lead["status"] == "lost"]
        )

        total_budget = sum(
            lead.get("budget", 0) or 0
            for lead in all_leads
        )

        average_budget = (
            total_budget / total_leads
            if total_leads > 0
            else 0
        )

        return {
            "total_leads": total_leads,
            "new_leads": new_leads,
            "contacted_leads": contacted_leads,
            "closed_leads": closed_leads,
            "lost_leads": lost_leads,
            "total_budget": total_budget,
            "average_budget": average_budget,
        }