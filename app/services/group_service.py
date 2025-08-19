from app.models import group
from app.models.gossip_lines import GossipLine
from app.models.proposal_line import ProposalLines
from app.models.group import Group
from app.models.user import User


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

    def propose(self, user: User) -> tuple[User, User, str]:
        if not self.group:
            raise ValueError("Group not found")
        pu = self.linked_user(user)
        proposal_line = ProposalLines.get_random_proposal_line(user)
        if not proposal_line:
            raise ValueError("No proposal line found for the user")
        message = proposal_line.content.replace(
            "{user1}", f"[{user.full_name()}]"
        ).replace("{user2}", f"[{pu.full_name()}]")
        return user, pu, message

    def gossip(self, user: User) -> tuple[User, str]:
        if not self.group:
            raise ValueError("Group not found")
        gossip_line = GossipLine.get_random_gossip_line(user)
        if not gossip_line:
            raise ValueError("No proposal line found for the user")
        message = gossip_line.content.replace("{user}", f"[{user.full_name()}]")
        return user, message

    def crush(self, user: User) -> tuple[User, User, str]:
        """Generate a random crush message for the user."""
        if not self.has_member(user):
            raise ValueError(f"User {user.full_name()} is not a member of the group.")
        proposed_user = self.group.propose_to(user)
        if proposed_user:
            message = f"{user.full_name()} has a crush on {proposed_user.full_name()}!"
            return user, proposed_user, message
        else:
            return user, user, "No crush found for you in this group."
