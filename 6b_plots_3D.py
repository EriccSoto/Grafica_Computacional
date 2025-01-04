from manim import *

class Todo(ThreeDScene):
    def construct(self):
        
        self.show_nombre()
        self.camera_position1()
        self.camera_position2()
        self.camera_position3()
        self.camera_position4()
        self.camera_position5()
        self.move_camera1()
        self.move_camera2()
        self.parametric_curve1()
        self.parametric_curve2()
        self.surfaces_animation()
        self.text3d1()
        self.text3d2()
        self.text3d3()
        self.show_nombres()
        
        
    def show_nombre(self):
        credit_text = Text("Hecho por Eric Carmen Soto")
        credit_text.to_edge(UP)
        self.play(Write(credit_text))
        self.wait(2)
        self.play(FadeOut(credit_text))  

    def camera_position1(self):
        self.camera.background_color = "#919b00"  
        axes = ThreeDAxes()
        circle = Circle()
        self.add(axes)
        self.play(Create(circle))
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def camera_position2(self):
        self.camera.background_color = "#33FF57"  # Verde brillante
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=30 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def camera_position3(self):
        self.camera.background_color = "#783b3b"  
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def camera_position4(self):
        self.camera.background_color = "#7a0666"  
        axes = ThreeDAxes(x_range=[-5, 5], y_range=[-5, 5], z_range=[-2, 2])
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def camera_position5(self):
        self.camera.background_color = "#8A2BE2"  # Azul violeta
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES, theta=45 * DEGREES, distance=6, gamma=30 * DEGREES)
        self.play(Create(circle), Create(axes))
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def move_camera1(self):
        self.camera.background_color = "#FF1493"  # Rosa fuerte
        axes = ThreeDAxes()
        circle = Circle()
        self.add(axes)
        self.play(Create(circle))
        self.move_camera(phi=30 * DEGREES, theta=-45 * DEGREES, run_time=3)
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def move_camera2(self):
        self.camera.background_color = "#09535b"  
        axes = ThreeDAxes()
        circle = Circle()
        self.set_camera_orientation(phi=80 * DEGREES)
        self.add(axes)
        self.play(Create(circle))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(5)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=80 * DEGREES, theta=-PI / 2)
        self.wait()
        self.play(FadeOut(circle), FadeOut(axes))

    def parametric_curve1(self):
        self.camera.background_color = "#FF4500"  # Naranja fuerte
        curve1_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            for u in np.linspace(-TAU, TAU, 100)
        ])
        curve1 = VMobject().set_points_as_corners(curve1_points)

        curve2_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            for u in np.linspace(-TAU, TAU, 100)
        ])
        curve2 = VMobject().set_points_as_corners(curve2_points)

        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
        self.play(FadeOut(curve1), FadeOut(curve2), FadeOut(axes))

    def parametric_curve2(self):
        self.camera.background_color = "#32CD32"  # Verde lima
        curve1_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u / 2]
            for u in np.linspace(-TAU, TAU, 100)
        ])
        curve1 = VMobject().set_points_as_corners(curve1_points).set_shade_in_3d(True)

        curve2_points = np.array([
            [1.2 * np.cos(u), 1.2 * np.sin(u), u]
            for u in np.linspace(-TAU, TAU, 100)
        ])
        curve2 = VMobject().set_points_as_corners(curve2_points).set_shade_in_3d(True)

        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(phi=80 * DEGREES, theta=-60 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        self.play(Create(curve1))
        self.wait()
        self.play(Transform(curve1, curve2), rate_func=there_and_back, run_time=3)
        self.wait()
        self.play(FadeOut(curve1), FadeOut(curve2), FadeOut(axes))

    def surfaces_animation(self):
        self.camera.background_color = "#FF6347"  # Tomate
        axes = ThreeDAxes()
        sphere = Surface(
            lambda u, v: np.array([
                1.5 * np.cos(u) * np.cos(v),
                1.5 * np.cos(u) * np.sin(v),
                1.5 * np.sin(u)
            ]),
            u_range=[-PI / 2, PI / 2],
            v_range=[0, TAU],
            checkerboard_colors=[RED_D, RED_E],
            resolution=(20, 40)
        ).scale(2).set_shade_in_3d(True)

        self.add(axes)
        self.set_camera_orientation(phi=75 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.2)
        self.play(Write(sphere))
        self.wait()
        self.play(FadeOut(sphere), FadeOut(axes))

    def text3d1(self):
        self.camera.background_color = "#D2691E"  # Chocolate
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Tex("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=RIGHT)
        self.add(axes, text3d)
        self.wait()
        self.play(FadeOut(text3d), FadeOut(axes))

    def text3d2(self):
        self.camera.background_color = "#DC143C"  # Rojo coral
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Text("This is a 3D text").scale(2)
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)
        self.begin_ambient_camera_rotation()
        self.play(Write(text3d))
        self.wait()
        self.play(FadeOut(text3d), FadeOut(axes))

    def text3d3(self):
        self.camera.background_color = "#7FFF00"  # Verde chartreuse
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        text3d = Tex("This is a 3D text").scale(2).set_shade_in_3d(True)
        text3d.rotate(PI / 2, axis=RIGHT)
        self.add(axes, text3d)
        self.wait()
        self.play(FadeOut(text3d), FadeOut(axes))

    def show_nombres(self):
        self.camera.background_color = "#614b8f"  
        credit_text = Text(
            "Universidad Autónoma del Estado de México\n"
            "Centro Universitario UAEM Zumpango\n"
            "Ingeniería en Computación\n"
            "GRAFICACIÓN COMPUTACIONAL\n\n"
            "Alumno: Eric Carmen Soto\n"
            "Segundo Periodo\n\n"
        ).scale(0.5) 
        
        credit_text.to_edge(ORIGIN) 
        credit_text.rotate(60 * DEGREES) 
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES)
        self.stop_ambient_camera_rotation()

        self.play(Write(credit_text))
        self.wait(5)  
        self.play(FadeOut(credit_text))
