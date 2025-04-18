from PyQt6.QtCore import QSettings, QVariantAnimation, pyqtProperty, QObject
from PyQt6.QtGui import QColor, QColorDialog

class ThemeController(QObject):
    def __init__(self, ui_handler):
        super().__init__()
        self.ui = ui_handler
        self.settings = QSettings("YourApp", "MusicManagementSystem")
        self.animation = QVariantAnimation()
        self.animation.valueChanged.connect(self._handle_animation_update)

    def apply_theme(self, theme_name):
        """Apply a predefined theme"""
        themes = {
            "default": ["#0A1828", "#178582", "#6C757D"],
            "simple": ["#f0f0f0", "#e0e0e0", "#d0d0d0"],
            "dark": ["#2b2b2b", "#3c3c3c", "#4d4d4d"],
            "light": ["#ffffff", "#eeeeee", "#dddddd"],
            "coffee": ["#cba987", "#a67c52", "#6f4e37"],
            "glass": ["#e0f7fa", "#b2ebf2", "#80deea"],
            "sunset": ["#ffccbc", "#ffab91", "#ff8a65"]
        }
        
        if theme_name in themes:
            colors = themes[theme_name]
            self._apply_colors(colors)
            self.settings.setValue("theme_name", theme_name)
            if theme_name == "custom":
                self.settings.setValue("custom_colors", colors)

    def set_custom_theme(self):
        """Handle custom theme creation"""
        colors = []
        for i in range(3):
            color = QColorDialog.getColor(title=f"Pick Color {i + 1}")
            if color.isValid():
                colors.append(color.name())
        
        if len(colors) == 3:
            self._apply_colors(colors)
            self.settings.setValue("theme_name", "custom")
            self.settings.setValue("custom_colors", colors)

    def load_last_theme(self):
        """Load theme from settings on startup"""
        theme_name = self.settings.value("theme_name", "default")
        if theme_name == "custom":
            colors = self.settings.value("custom_colors", ["#0A1828", "#178582", "#6C757D"])
            if colors and len(colors) == 3:
                self._apply_colors(colors)
        else:
            self.apply_theme(theme_name)

    def animate_label_bg(self, label, start_color, end_color, duration=400):
        """Animate background color transitions"""
        self.animation.setStartValue(QColor(start_color))
        self.animation.setEndValue(QColor(end_color))
        self.animation.setDuration(duration)
        self.animation.setTargetObject(label)
        self.animation.start()

    def _apply_colors(self, colors):
        """Apply colors to all UI elements"""
        if len(colors) != 3:
            return

        color1, color2, color3 = colors
        
        # Animate main background
        self._animate_bg_element(self.ui.bg_body, color1)
        
        # Animate header background
        self._animate_bg_element(self.ui.bg_head, color2)
        
        # Animate other backgrounds
        for attr in dir(self.ui):
            if attr.startswith("bg_") and attr not in ["bg_body", "bg_head"]:
                element = getattr(self.ui, attr)
                if hasattr(element, "setStyleSheet"):
                    self._animate_bg_element(element, color3)

    def _animate_bg_element(self, element, end_color):
        """Animate individual background element"""
        current_color = element.palette().window().color().name()
        self.animate_label_bg(element, current_color, end_color)

    def _handle_animation_update(self, value):
        """Update style during animation"""
        target = self.animation.targetObject()
        if target:
            target.setStyleSheet(f"background-color: {value.name()}; border-radius: 5px;")