# Created by Jessel56 on 2025-07-24 23:57:13
# Enhanced Manim XBlock with 3D support and advanced features

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String, Dict, Integer, Boolean
import pkg_resources
import json
import tempfile
import os
from manim import *

class ManimXBlock(XBlock):
    """
    Enhanced XBlock for rendering Manim math animations with advanced features.
    """
    
    display_name = String(
        display_name="Display Name",
        default="Manim Animation",
        scope=Scope.settings,
        help="Name of the animation component"
    )
    
    animation_data = Dict(
        display_name="Animation Data",
        default={
            "type": "default",
            "preset": "hello_manim",
            "quality": "medium",
            "fps": 30,
            "theme": "dark",
            "show_code": True,
            "code": """from manim import *
class HelloManimScene(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)"""
        },
        scope=Scope.content,
        help="Manim animation code and settings"
    )

    # Additional settings
    fps = Integer(
        display_name="Frame Rate",
        default=30,
        scope=Scope.settings,
        help="Animation frame rate (FPS)"
    )
    
    show_code = Boolean(
        display_name="Show Code",
        default=True,
        scope=Scope.settings,
        help="Whether to display the code below the animation"
    )

    # Extended preset animations
    PRESETS = {
        "hello_manim": {
            "name": "Hello Manim",
            "description": "Basic text animation",
            "code": """from manim import *
class HelloManimScene(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))
        self.wait(2)"""
        },
        "circle_transform": {
            "name": "Circle Transform",
            "description": "Shape transformation",
            "code": """from manim import *
class CircleTransformScene(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait()"""
        },
        "math_equation": {
            "name": "Math Equation",
            "description": "LaTeX math rendering",
            "code": """from manim import *
class MathEquationScene(Scene):
    def construct(self):
        equation = MathTex(r"\int_{a}^{b} x^2 dx")
        self.play(Write(equation))
        self.wait(2)"""
        },
        "neural_network": {
            "name": "Neural Network",
            "description": "Dynamic neural network visualization",
            "code": """from manim import *
class NeuralNetworkScene(Scene):
    def construct(self):
        network = VGroup()
        layers = [3, 4, 4, 2]
        
        for i, layer_size in enumerate(layers):
            layer = VGroup()
            for j in range(layer_size):
                neuron = Circle(radius=0.2, color=BLUE)
                neuron.move_to([2*i - 3, 2*j - layer_size + 1, 0])
                layer.add(neuron)
            network.add(layer)
            
            if i > 0:
                for neuron1 in network[i-1]:
                    for neuron2 in layer:
                        connection = Line(neuron1, neuron2, color=GRAY)
                        network.add(connection)
        
        self.play(Create(network))
        self.wait(2)"""
        },
        "molecule_3d": {
            "name": "3D Molecule",
            "description": "3D molecule visualization",
            "code": """from manim import *
class Molecule3DScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        molecule = VGroup()
        
        # Create atoms
        atoms = [
            (Sphere(radius=0.3).set_color(RED), [0, 0, 0]),    # Central atom
            (Sphere(radius=0.2).set_color(BLUE), [1, 1, 1]),   # Outer atoms
            (Sphere(radius=0.2).set_color(BLUE), [-1, 1, -1]),
            (Sphere(radius=0.2).set_color(BLUE), [1, -1, -1]),
            (Sphere(radius=0.2).set_color(BLUE), [-1, -1, 1])
        ]
        
        # Add atoms and bonds
        for atom, pos in atoms:
            atom.move_to(np.array(pos))
            molecule.add(atom)
            if pos != [0, 0, 0]:  # Add bonds to central atom
                bond = Cylinder(radius=0.05, height=np.linalg.norm(pos))
                bond.rotate(angle=np.arccos(pos[2]/np.linalg.norm(pos)))
                bond.move_to((np.array(pos) + np.zeros(3))/2)
                molecule.add(bond)
        
        self.play(Create(molecule))
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(5)
        self.stop_ambient_camera_rotation()"""
        }
    }

    def student_view(self, context=None):
        """Enhanced student view with advanced controls"""
        html = self.resource_string("static/html/manim_viewer.html")
        frag = Fragment(html.format(
            animation_id=self._get_unique_id(),
            video_url=self._get_video_url(),
            animation_data=json.dumps(self.animation_data),
            show_code=json.dumps(self.show_code)
        ))
        
        frag.add_css(self.resource_string("static/css/manim_viewer.css"))
        frag.add_javascript(self.resource_string("static/js/manim_viewer.js"))
        frag.initialize_js("ManimXBlock", {
            "animationData": self.animation_data,
            "fps": self.fps,
            "showCode": self.show_code
        })
        return frag

    def studio_view(self, context=None):
        """Enhanced Studio editing view"""
        html = self.resource_string("static/html/manim_editor.html")
        frag = Fragment(html.format(
            animation_data=json.dumps(self.animation_data, indent=2),
            presets=json.dumps(self.PRESETS),
            fps=self.fps,
            show_code=json.dumps(self.show_code)
        ))
        
        frag.add_css(self.resource_string("static/css/manim_editor.css"))
        frag.add_javascript(self.resource_string("static/js/manim_editor.js"))
        frag.initialize_js("ManimXBlockEditor", {
            "presets": self.PRESETS,
            "handlerUrl": self.runtime.handler_url(self, 'save_settings')
        })
        return frag

    @XBlock.json_handler
    def save_settings(self, data, suffix=""):
        """Save all settings"""
        self.animation_data = data.get('animation_data', self.animation_data)
        self.fps = data.get('fps', self.fps)
        self.show_code = data.get('show_code', self.show_code)
        return {
            "status": "success",
            "video_url": self._get_video_url()
        }

    def _get_video_url(self):
        """Get or generate video URL"""
        try:
            video_path = self._render_animation()
            return video_path if video_path else ""
        except Exception as e:
            log.error(f"Failed to get video URL: {e}")
            return ""

    def _render_animation(self):
        """Render animation using Manim"""
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                # Save animation code
                code_path = os.path.join(tmpdir, "animation.py")
                with open(code_path, "w") as f:
                    f.write(self.animation_data["code"])
                
                # Configure renderer
                config.media_dir = tmpdir
                config.video_dir = tmpdir
                config.quality = self.animation_data.get("quality", "medium")
                config.frame_rate = self.fps
                
                # Import and render scene
                scene_class = self._get_scene_class()
                scene = scene_class()
                scene.render()
                
                # Get output path
                return scene.renderer.file_writer.movie_file_path
        except Exception as e:
            log.error(f"Animation rendering failed: {e}")
            return None

    def _get_scene_class(self):
        """Extract scene class from code"""
        namespace = {}
        exec(self.animation_data["code"], namespace)
        return next(v for v in namespace.values() 
                   if isinstance(v, type) and issubclass(v, Scene))

    def _get_unique_id(self):
        """Generate unique ID for animation container"""
        return f"manim-{self.scope_ids.usage_id.block_id}"
