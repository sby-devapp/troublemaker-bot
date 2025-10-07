from app.models import group
from app.models.crush_lines import CrushLine
from app.models.gossip_lines import GossipLine
from app.models.proposal_line import ProposalLines
from app.models.group import Group
from app.models.user import User
from utils.html_parse import format_mention_html


class GroupService:
    def __init__(self, group_or_id=None):
        """Initialize the GroupService with a group or group ID."""
        print("Group service initialized")
        if isinstance(group_or_id, Group):
            self.group = group_or_id
        elif isinstance(group_or_id, int):
            self.group = Group(id=group_or_id).get() if group_or_id else None
        else:
            self.group = None

    def linked_user(self, user: User) -> User:
        if not self.group:
            raise ValueError("Group not found")
        linked_user = user.link_me_with_from_group(self.group)
        if not linked_user:
            raise ValueError("No linked user found in the group")

        return linked_user

    def has_member(self, user: User) -> bool:
        """Check if a user is registered in the group."""
        if not self.group:
            raise ValueError("Group not found")
        return self.group.has_member(user)

    def register(self, user: User) -> User:
        """Register a user in the group."""
        if not self.group:
            raise ValueError("Group not found")
        self.group.add_member(user)
        return user

    def propose(self, targetuser: User) -> tuple[User, User, str]:
        if not self.group:
            raise ValueError("Group not found")
        proposal_user = self.linked_user(targetuser)
        proposal_line = ProposalLines.get_random_proposal_line(targetuser)
        if not proposal_line:
            raise ValueError("No proposal line found for the user")
        message = proposal_line.content.replace(
            "{user1}", f"<b>{format_mention_html(targetuser)}</b>"
        ).replace("{user2}", f"<b>{format_mention_html(proposal_user)}</b>")
        return targetuser, proposal_user, message

    def gossip(self, targetuser: User) -> tuple[User, str]:
        if not self.group:
            raise ValueError("Group not found")
        gossip_line = GossipLine.get_random_gossip_line(targetuser)
        if not gossip_line:
            raise ValueError("No proposal line found for the user")
        message = gossip_line.content.replace("{user}", f"<b>{format_mention_html(targetuser)}</b>")
        return targetuser, message

    def crush(self, targetuser: User) -> tuple[User, User, str]:
        """Generate a random crush message for the user."""
        if not self.has_member(targetuser):
            raise ValueError(f"User {targetuser.full_name()} is not a member of the group.")
        crush_user = self.group.propose_to(targetuser)
        if crush_user:

            crush_line = CrushLine.get_random_crush_line(targetuser)
            if not crush_line:
                raise ValueError("No crush line found for the user")
            else:
                
                crush_line_content = crush_line.content.replace(
                    "{targetuser}", f"<b>{format_mention_html(targetuser)}</b>"
                ).replace("{crushuser}", f"<b>{format_mention_html(crush_user)}</b>")
                if crush_line.topic.lower() == "annoyed":
                   crush_user = None
                print("message: "+crush_line_content)
            return targetuser, crush_user, crush_line_content
        else:
            return targetuser, targetuser, "No crush found for you in this group."

    def participate_to_game(self, user: User, key: bool) -> User:
        """Participate/logout to the game in the group."""
        if not self.group:
            raise ValueError("Group not found")
        self.group.participate_to_game(user, key)
        return user


    def is_participant(self, user: "User"):
        if not self.group:
            raise ValueError("Group not found")
        return self.group.is_participant(user)