from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String

class PaymentTierXBlock(XBlock):
    """XBlock for handling payment tiers and gated content."""
    
    display_name = String(
        display_name="Display Name",
        default="Payment Tier Gate",
        scope=Scope.settings,
        help="Name of the payment tier gate"
    )
    
    required_tier = String(
        display_name="Required Tier",
        default="free",
        scope=Scope.settings,
        help="Minimum payment tier required"
    )

    def student_view(self, context=None):
        """Show the gated content view."""
        html = "<div>Content requires {tier} access</div>".format(
            tier=self.required_tier
        )
        return Fragment(html)
