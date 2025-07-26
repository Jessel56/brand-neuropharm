from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String
import pkg_resources

class MoleculeExplorerXBlock(XBlock):
    """XBlock for exploring molecular structures."""
    
    display_name = String(
        display_name="Display Name",
        default="Molecule Explorer",
        scope=Scope.settings,
        help="Name of the molecule explorer"
    )
    
    molecule_data = String(
        display_name="Molecule Data",
        default="{}",
        scope=Scope.content,
        help="JSON data for molecule rendering"
    )

    def resource_string(self, path):
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """Show the molecule explorer view."""
        html = self.resource_string("static/html/molecule_explorer.html")
        frag = Fragment(html)
        frag.add_css(self.resource_string("static/css/molecule_explorer.css"))
        frag.add_javascript(self.resource_string("static/js/molecule_explorer.js"))
        frag.initialize_js("MoleculeExplorerXBlock")
        return frag
