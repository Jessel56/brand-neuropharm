# File: tutor-plugins-root/neuropharm.py
import os
import pkg_resources
from tutor import hooks

# Plugin Specification
__version__ = "21.0.0" # Updated version

config = {
    "defaults": {
        # --- VERSIONING ---
        # Using specific tags or commit hashes is CRITICAL for reproducible builds.
        # Never use 'main' or 'master' in production.
        "NEUROPHARM_BRAND_REPO": "https://github.com/Jessel56/brand-neuropharm.git",
        "NEUROPHARM_BRAND_VERSION": "v1.6.9", # Use a specific tag
        ##"XBLOCK_MOLECULE_VIEWER_REPO": "https://github.com/YourOrganization/xblock-molviewer.git",
        ##"XBLOCK_MOLECULE_VIEWER_VERSION": "v1.0.1",
        ##"XBLOCK_CASE_STUDY_REPO": "https://github.com/YourOrganization/xblock-casestudy.git",
        #"XBLOCK_CASE_STUDY_VERSION": "v1.1.0",
        "XBLOCK_MANIM_REPO": "https://github.com/Jessel56/xblock-manim.git",
        "XBLOCK_MANIM_VERSION": "v1.6.9",
    },
    "unique": {},
    "patches": {
        # This patch tells openedx to use our comprehensive theme.
        # The 404/500 templates are now handled automatically by placing them
        # in the correct theme directory, so the Python override is removed.
        "openedx-lms-common-settings": """
COMPREHENSIVE_THEME_DIRS.append(str(Path(TUTOR_ROOT) / "env" / "build" / "openedx" / "themes"))
THEME_NAME = "neuropharm"
""",
        # This patch adds our custom certificate template.
        "openedx-lms-production-settings": """
CERTIFICATE_TEMPLATES.append(
    {
        "id": "neuropharm_default",
        "name": "Neuropharm Academy Default Certificate",
        "template": "neuropharm/certificate/template.html",
        "preview_image": "neuropharm/certificate/preview.png",
        "mode": "honor"
    }
)
""",
        # This patch installs our custom XBlocks into the python environment.
        "openedx-dockerfile-post-python-requirements": """
# Install custom XBlocks for Neuropharm Academy using specific versions
pip install git+{{ XBLOCK_MANIM_REPO }}@{{ XBLOCK_MANIM_VERSION }}
""",
    },
}

# Plugin Hooks
@hooks.Actions.PROJECT_ROOT_LOADED.add()
def copy_theme_assets(project_root):
    # Copy the comprehensive theme
    source_theme_path = pkg_resources.resource_filename("neuropharm", "theme")
    dest_theme_path = os.path.join(project_root, "env", "build", "openedx", "themes", "neuropharm")
    hooks.actions.symlink_or_copy(source_theme_path, dest_theme_path)

    # Copy the certificate assets
    source_cert_path = pkg_resources.resource_filename("neuropharm", "assets/certificate")
    dest_cert_path = os.path.join(project_root, "env", "build", "openedx", "lms", "static", "neuropharm", "certificate")
    hooks.actions.symlink_or_copy(source_cert_path, dest_cert_path)

# This hook patches the MFE Dockerfile to install your custom brand package.
@hooks.Filters.ENV_PATCHES.add_item(
    (
        "mfe-dockerfile-post-npm-install",
        """
# Install the Neuropharm Academy brand package using a specific version
RUN npm install "@openedx/brand@{{ NEUROPHARM_BRAND_REPO }}#{{ NEUROPHARM_BRAND_VERSION }}" --force
"""
    )
)
