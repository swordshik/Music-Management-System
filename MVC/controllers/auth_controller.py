from PyQt6.QtWidgets import QMessageBox, QInputDialog
from PyQt6.QtGui import QLineEdit
import re

class AuthController:
    def __init__(self, user_dao, ui_handlers):
        self.user_dao = user_dao
        self.ui = ui_handlers
        self.current_user = None

    def handle_login(self):
        """Handle the complete login/signup flow"""
        name = self.ui.get_name_input().strip()
        email = self.ui.get_email_input().strip()
        password = self.ui.get_password_input().strip()

        if not all([name, email, password]):
            self.show_warning("Input Error", "Please fill all fields")
            return

        # Attempt login
        user = self.user_dao.get_user(email, password)
        if user:
            self._handle_successful_login(user)
            return

        # Handle new user creation
        if self.user_dao.email_exists(email):
            self.show_warning("Login Failed", "Incorrect password")
            return

        if self._create_new_user(name, email, password):
            self.show_info("Success", "Account created! Please log in")
            self.ui.clear_login_fields()

    def handle_password_reset(self):
        """Handle password reset workflow"""
        email, ok = QInputDialog.getText(
            self.ui.main_window, 
            "Reset Password", 
            "Enter your email:"
        )
        if not ok or not email:
            return

        user_id, ok = QInputDialog.getInt(
            self.ui.main_window,
            "Reset Password",
            "Enter your User ID:"
        )
        if not ok:
            return

        if not self._verify_user(email, user_id):
            self.show_warning("Invalid", "No matching user found")
            return

        new_password, confirmed_password = self._get_new_passwords()
        if not new_password:
            return

        if not self._validate_new_password(new_password, confirmed_password):
            return

        self.user_dao.update_password(user_id, new_password)
        self.show_info("Success", "Password updated successfully!")

    def _handle_successful_login(self, user):
        """Update state after successful login"""
        self.current_user = {
            "id": user[0],
            "name": user[1],
            "email": user[2],
            "is_admin": "Admin" if user[3] else "User"
        }
        self.ui.update_ui_after_login(self.current_user)
        self.show_info("Welcome", f"Welcome {self.current_user['name']}!")

    def _create_new_user(self, name, email, password):
        """Handle new user creation with validation"""
        if not self._validate_password_strength(password):
            return False

        if not self._validate_email(email):
            return False

        if not self.user_dao.create_user(name, email, password):
            self.show_warning("Error", "Email already exists")
            return False

        return True

    def _validate_password_strength(self, password):
        """Check password meets strength requirements"""
        if len(password) < 8:
            self.show_warning(
                "Weak Password",
                "Password must be at least 8 characters"
            )
            return False
        if not re.search(r"[A-Z]", password) or not re.search(r"\d", password):
            self.show_warning(
                "Weak Password",
                "Password must contain at least one uppercase letter and one number"
            )
            return False
        return True

    def _validate_email(self, email):
        """Basic email validation"""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Invalid Email", "Please enter a valid email address")
            return False
        return True

    def _get_new_passwords(self):
        """Get and confirm new password"""
        new_pass, ok1 = QInputDialog.getText(
            self.ui.main_window,
            "New Password",
            "Enter new password:",
            echoMode=QLineEdit.Password
        )
        confirm_pass, ok2 = QInputDialog.getText(
            self.ui.main_window,
            "Confirm Password",
            "Re-enter password:",
            echoMode=QLineEdit.Password
        )
        return (new_pass.strip(), confirm_pass.strip()) if ok1 and ok2 else (None, None)

    def _validate_new_password(self, new_pass, confirm_pass):
        """Validate new password requirements"""
        if new_pass != confirm_pass:
            self.show_warning("Mismatch", "Passwords do not match")
            return False
        return self._validate_password_strength(new_pass)

    def _verify_user(self, email, user_id):
        """Verify user exists with given email and ID"""
        user = self.user_dao.get_user_by_id(user_id)
        return user and user[2] == email  # Check email matches

    def show_warning(self, title, message):
        QMessageBox.warning(self.ui.main_window, title, message)

    def show_info(self, title, message):
        QMessageBox.information(self.ui.main_window, title, message)