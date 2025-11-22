import json
import os
from datetime import datetime


# Base User Class
class User:
    """Base class for all user types with common attributes and methods"""

    def __init__(self, username, name, industry, bio):
        self.username = username
        self.name = name
        self.industry = industry
        self.bio = bio
        self.role = "User"
        self.connections = []
        self.pending_requests = []
        self.sent_requests = []
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def view_dashboard(self):
        """Display user's dashboard with profile info and connections"""
        print("\n" + "=" * 60)
        print(f"{'DASHBOARD - ' + self.name:^60}")
        print("=" * 60)
        print(f"Username: {self.username}")
        print(f"Role: {self.role}")
        print(f"Industry: {self.industry}")
        print(f"Bio: {self.bio}")
        print(f"Connections: {len(self.connections)}")
        print(f"Pending Requests: {len(self.pending_requests)}")
        print("=" * 60)

    def display_profile(self):
        """Display basic profile information"""
        print(f"\nName: {self.name}")
        print(f"Username: @{self.username}")
        print(f"Role: {self.role}")
        print(f"Industry: {self.industry}")
        print(f"Bio: {self.bio}")

    def send_connection_request(self, target_user):
        """Send a connection request to another user"""
        if target_user.username == self.username:
            return "Cannot send request to yourself"

        if target_user.username in self.connections:
            return "Already connected with this user"

        if target_user.username in self.sent_requests:
            return "Request already sent to this user"

        # Add to sender's sent requests
        self.sent_requests.append(target_user.username)
        # Add to receiver's pending requests
        target_user.pending_requests.append(self.username)

        return f"Connection request sent to {target_user.name}"

    def accept_request(self, requester_username, all_users):
        """Accept a connection request"""
        if requester_username not in self.pending_requests:
            return "No pending request from this user"

        # Remove from pending requests
        self.pending_requests.remove(requester_username)

        # Add to connections for both users
        self.connections.append(requester_username)

        # Find requester and update their connections
        for user in all_users:
            if user.username == requester_username:
                user.connections.append(self.username)
                if self.username in user.sent_requests:
                    user.sent_requests.remove(self.username)
                break

        return f"Connection accepted with @{requester_username}"

    def decline_request(self, requester_username, all_users):
        """Decline a connection request"""
        if requester_username not in self.pending_requests:
            return "No pending request from this user"

        self.pending_requests.remove(requester_username)

        # Remove from requester's sent requests
        for user in all_users:
            if user.username == requester_username:
                if self.username in user.sent_requests:
                    user.sent_requests.remove(self.username)
                break

        return f"Connection declined from @{requester_username}"

    def view_matches(self, all_users):
        """Find and display matching users based on industry"""
        matches = []
        for user in all_users:
            # Match based on industry and exclude self and existing connections
            if (user.industry == self.industry and
                    user.username != self.username and
                    user.username not in self.connections):
                matches.append(user)
        return matches

    def to_dict(self):
        """Convert user object to dictionary for JSON storage"""
        return {
            'username': self.username,
            'name': self.name,
            'industry': self.industry,
            'bio': self.bio,
            'role': self.role,
            'connections': self.connections,
            'pending_requests': self.pending_requests,
            'sent_requests': self.sent_requests,
            'created_at': self.created_at
        }


# Child Class: Startup Founder
class StartupFounder(User):
    """Class for startup founders with specific attributes"""

    def __init__(self, username, name, industry, bio, startup_name, duration, scale):
        super().__init__(username, name, industry, bio)
        self.role = "Startup Founder"
        self.startup_name = startup_name
        self.duration = duration
        self.scale = scale

    def display_profile(self):
        """Override to show startup-specific details"""
        super().display_profile()
        print(f"Startup Name: {self.startup_name}")
        print(f"Operating Duration: {self.duration}")
        print(f"Scale: {self.scale}")

    def view_matches(self, all_users):
        """Founders match with Mentors and Investors"""
        matches = []
        for user in all_users:
            # Match with Mentors and Investors in same industry
            if (user.industry == self.industry and
                    user.username != self.username and
                    user.username not in self.connections and
                    user.role in ["Mentor", "Investor"]):
                matches.append(user)
        return matches

    def to_dict(self):
        """Convert to dictionary including startup-specific fields"""
        data = super().to_dict()
        data.update({
            'startup_name': self.startup_name,
            'duration': self.duration,
            'scale': self.scale
        })
        return data


# Child Class: Mentor
class Mentor(User):
    """Class for mentors with specific attributes"""

    def __init__(self, username, name, industry, bio, expertise, years_experience):
        super().__init__(username, name, industry, bio)
        self.role = "Mentor"
        self.expertise = expertise
        self.years_experience = years_experience

    def display_profile(self):
        """Override to show mentor-specific details"""
        super().display_profile()
        print(f"Expertise: {self.expertise}")
        print(f"Years of Experience: {self.years_experience}")

    def view_matches(self, all_users):
        """Mentors match with Startup Founders"""
        matches = []
        for user in all_users:
            if (user.industry == self.industry and
                    user.username != self.username and
                    user.username not in self.connections and
                    user.role == "Startup Founder"):
                matches.append(user)
        return matches

    def to_dict(self):
        """Convert to dictionary including mentor-specific fields"""
        data = super().to_dict()
        data.update({
            'expertise': self.expertise,
            'years_experience': self.years_experience
        })
        return data


# Child Class: Investor
class Investor(User):
    """Class for investors with specific attributes"""

    def __init__(self, username, name, industry, bio, investment_range, investment_stage):
        super().__init__(username, name, industry, bio)
        self.role = "Investor"
        self.investment_range = investment_range
        self.investment_stage = investment_stage

    def display_profile(self):
        """Override to show investor-specific details"""
        super().display_profile()
        print(f"Investment Range: {self.investment_range}")
        print(f"Investment Stage: {self.investment_stage}")

    def view_matches(self, all_users):
        """Investors match with Startup Founders"""
        matches = []
        for user in all_users:
            if (user.industry == self.industry and
                    user.username != self.username and
                    user.username not in self.connections and
                    user.role == "Startup Founder"):
                matches.append(user)
        return matches

    def to_dict(self):
        """Convert to dictionary including investor-specific fields"""
        data = super().to_dict()
        data.update({
            'investment_range': self.investment_range,
            'investment_stage': self.investment_stage
        })
        return data


# Data Management Functions
class DataManager:
    """Handles saving and loading user data to/from JSON file"""

    DATA_FILE = "startup_connect_data.json"

    @staticmethod
    def save_users(users):
        """Save all users to JSON file"""
        data = [user.to_dict() for user in users]
        with open(DataManager.DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def load_users():
        """Load users from JSON file and recreate user objects"""
        if not os.path.exists(DataManager.DATA_FILE):
            return []

        try:
            with open(DataManager.DATA_FILE, 'r') as f:
                data = json.load(f)

            users = []
            for user_data in data:
                role = user_data['role']

                if role == "Startup Founder":
                    user = StartupFounder(
                        user_data['username'],
                        user_data['name'],
                        user_data['industry'],
                        user_data['bio'],
                        user_data['startup_name'],
                        user_data['duration'],
                        user_data['scale']
                    )
                elif role == "Mentor":
                    user = Mentor(
                        user_data['username'],
                        user_data['name'],
                        user_data['industry'],
                        user_data['bio'],
                        user_data['expertise'],
                        user_data['years_experience']
                    )
                elif role == "Investor":
                    user = Investor(
                        user_data['username'],
                        user_data['name'],
                        user_data['industry'],
                        user_data['bio'],
                        user_data['investment_range'],
                        user_data['investment_stage']
                    )
                else:
                    continue

                # Restore connections and requests
                user.connections = user_data.get('connections', [])
                user.pending_requests = user_data.get('pending_requests', [])
                user.sent_requests = user_data.get('sent_requests', [])
                user.created_at = user_data.get('created_at', '')

                users.append(user)

            return users
        except Exception as e:
            print(f"Error loading data: {e}")
            return []


# Main Application Class
class StartupConnect:
    """Main application controller"""

    def __init__(self):
        self.users = DataManager.load_users()
        self.current_user = None

    def run(self):
        """Main program loop"""
        while True:
            if self.current_user is None:
                self.show_welcome_menu()
            else:
                self.show_logged_in_menu()

    def show_welcome_menu(self):
        """Display welcome menu for non-logged-in users"""
        print("\n" + "=" * 60)
        print(f"{'STARTUP CONNECT':^60}")
        print(f"{'Connect Founders, Mentors & Investors':^60}")
        print("=" * 60)
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            self.register_user()
        elif choice == "2":
            self.login_user()
        elif choice == "3":
            self.exit_program()
        else:
            print("Invalid choice. Please try again.")

    def register_user(self):
        """Handle user registration"""
        print("\n" + "-" * 60)
        print("USER REGISTRATION")
        print("-" * 60)

        # Select role
        print("\nSelect your role:")
        print("1. Startup Founder")
        print("2. Mentor")
        print("3. Investor")

        role_choice = input("\nEnter choice (1-3): ").strip()

        if role_choice not in ["1", "2", "3"]:
            print("Invalid role selection.")
            return

        # Common details
        username = input("\nEnter username: ").strip()

        # Check if username already exists
        if any(user.username == username for user in self.users):
            print("Username already exists. Please choose another.")
            return

        name = input("Enter full name: ").strip()
        industry = input("Enter industry (e.g., FinTech, HealthTech, EdTech): ").strip()
        bio = input("Enter a short bio: ").strip()

        # Role-specific details
        if role_choice == "1":
            startup_name = input("Enter startup name: ").strip()
            duration = input("Duration of operations (e.g., 2 years): ").strip()
            scale = input("Scale (Early Stage/Growth Stage/Mature): ").strip()

            user = StartupFounder(username, name, industry, bio, startup_name, duration, scale)

        elif role_choice == "2":
            expertise = input("Enter expertise area (e.g., Marketing, Product Development): ").strip()
            years = input("Years of experience: ").strip()

            user = Mentor(username, name, industry, bio, expertise, years)

        elif role_choice == "3":
            inv_range = input("Investment range (e.g., $10K-$50K): ").strip()
            inv_stage = input("Investment stage (Seed/Series A/Series B): ").strip()

            user = Investor(username, name, industry, bio, inv_range, inv_stage)

        self.users.append(user)
        DataManager.save_users(self.users)

        print(f"\n✓ Registration successful! Welcome, {name}!")
        print("You can now login with your username.")

    def login_user(self):
        """Handle user login"""
        print("\n" + "-" * 60)
        print("USER LOGIN")
        print("-" * 60)

        username = input("\nEnter username: ").strip()

        user = next((u for u in self.users if u.username == username), None)

        if user:
            self.current_user = user
            print(f"\n✓ Welcome back, {user.name}!")
        else:
            print("Username not found. Please register first.")

    def show_logged_in_menu(self):
        """Display menu for logged-in users"""
        print("\n" + "=" * 60)
        print(f"{'MAIN MENU':^60}")
        print("=" * 60)
        print("\n1. View Dashboard")
        print("2. Find Matches")
        print("3. View Connection Requests")
        print("4. View My Connections")
        print("5. Logout")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            self.current_user.view_dashboard()
        elif choice == "2":
            self.find_matches()
        elif choice == "3":
            self.view_requests()
        elif choice == "4":
            self.view_connections()
        elif choice == "5":
            self.logout()
        else:
            print("Invalid choice. Please try again.")

    def find_matches(self):
        """Find and display matching users"""
        print("\n" + "-" * 60)
        print("FIND MATCHES")
        print("-" * 60)

        matches = self.current_user.view_matches(self.users)

        if not matches:
            print("\nNo matches found in your industry.")
            return

        print(f"\nFound {len(matches)} match(es):\n")

        for idx, user in enumerate(matches, 1):
            print(f"{idx}. ", end="")
            user.display_profile()
            print("-" * 40)

        # Option to send connection request
        choice = input("\nEnter number to send connection request (or 0 to go back): ").strip()

        if choice == "0":
            return

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(matches):
                result = self.current_user.send_connection_request(matches[choice_idx])
                print(f"\n{result}")
                DataManager.save_users(self.users)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def view_requests(self):
        """View and manage connection requests"""
        print("\n" + "-" * 60)
        print("CONNECTION REQUESTS")
        print("-" * 60)

        if not self.current_user.pending_requests:
            print("\nNo pending connection requests.")
            return

        print(f"\nYou have {len(self.current_user.pending_requests)} pending request(s):\n")

        for idx, username in enumerate(self.current_user.pending_requests, 1):
            user = next((u for u in self.users if u.username == username), None)
            if user:
                print(f"{idx}. Request from {user.name} (@{user.username})")
                print(f"   Role: {user.role} | Industry: {user.industry}")
                print("-" * 40)

        # Option to respond to request
        choice = input("\nEnter number to respond to request (or 0 to go back): ").strip()

        if choice == "0":
            return

        try:
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(self.current_user.pending_requests):
                username = self.current_user.pending_requests[choice_idx]
                action = input(f"\nAccept or Decline request from @{username}? (a/d): ").strip().lower()

                if action == 'a':
                    result = self.current_user.accept_request(username, self.users)
                    print(f"\n{result}")
                elif action == 'd':
                    result = self.current_user.decline_request(username, self.users)
                    print(f"\n{result}")
                else:
                    print("Invalid action.")

                DataManager.save_users(self.users)
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input.")

    def view_connections(self):
        """View established connections"""
        print("\n" + "-" * 60)
        print("MY CONNECTIONS")
        print("-" * 60)

        if not self.current_user.connections:
            print("\nYou have no connections yet. Start finding matches!")
            return

        print(f"\nYou are connected with {len(self.current_user.connections)} user(s):\n")

        for idx, username in enumerate(self.current_user.connections, 1):
            user = next((u for u in self.users if u.username == username), None)
            if user:
                print(f"{idx}. {user.name} (@{user.username})")
                print(f"   Role: {user.role} | Industry: {user.industry}")
                print("-" * 40)

    def logout(self):
        """Logout current user"""
        print(f"\n✓ Goodbye, {self.current_user.name}!")
        self.current_user = None

    def exit_program(self):
        """Exit the application"""
        print("\n" + "=" * 60)
        print("Thank you for using Startup Connect!")
        print("=" * 60)
        exit()


# Entry Point
if __name__ == "__main__":
    app = StartupConnect()
    app.run()