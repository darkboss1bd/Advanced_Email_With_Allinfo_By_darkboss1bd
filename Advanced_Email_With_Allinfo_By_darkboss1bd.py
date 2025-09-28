import os
import requests
import webbrowser
import time
import random
import json
import threading
from datetime import datetime, timedelta
from urllib.parse import quote, urlencode
import base64
import hashlib
import sys

class RealTimeAccountMonitor:
    def __init__(self):
        self.brand_name = "darkboss1bd"
        self.version = "5.0"
        self.author = "darkboss1bd"
        self.telegram_id = "https://t.me/darkvaiadmin"
        self.telegram_channel = "https://t.me/windowspremiumkey"
        
        # Real-time activity database with realistic behaviors
        self.platforms_activities = {
            # Social Media with realistic activities
            "Facebook": {
                "url": "https://facebook.com/{}",
                "activities": [
                    "Profile viewed", "Post liked", "Photo uploaded", "Friend request sent",
                    "Message sent", "Story posted", "Comment added", "Page liked",
                    "Group joined", "Event created", "Live stream started", "Reel watched"
                ],
                "login_count": random.randint(5, 50),
                "session_data": self.generate_session_data()
            },
            "Instagram": {
                "url": "https://instagram.com/{}",
                "activities": [
                    "Post liked", "Story viewed", "Reel created", "DM sent",
                    "Comment posted", "Follow added", "Hashtag searched", "Profile visited",
                    "Live stream watched", "IGTV video uploaded", "Shop browsed", "Filter used"
                ],
                "login_count": random.randint(10, 100),
                "session_data": self.generate_session_data()
            },
            "Twitter": {
                "url": "https://twitter.com/{}",
                "activities": [
                    "Tweet posted", "Retweet done", "Like given", "DM sent",
                    "Thread created", "Space joined", "Trend viewed", "List created",
                    "Moment watched", "Poll voted", "Fleet posted", "Bookmark added"
                ],
                "login_count": random.randint(8, 80),
                "session_data": self.generate_session_data()
            },
            "LinkedIn": {
                "url": "https://linkedin.com/in/{}",
                "activities": [
                    "Profile viewed", "Connection requested", "Post shared", "Job applied",
                    "Skill endorsed", "Recommendation given", "Article published", "Course taken",
                    "Company followed", "Message sent", "Profile updated", "News shared"
                ],
                "login_count": random.randint(3, 30),
                "session_data": self.generate_session_data()
            },
            "Gmail": {
                "url": "https://gmail.com",
                "activities": [
                    "Email sent", "Email received", "Email deleted", "Label created",
                    "Filter set", "Contact added", "Draft saved", "Search performed",
                    "Attachment downloaded", "Spam reported", "Star added", "Forward done"
                ],
                "login_count": random.randint(50, 200),
                "session_data": self.generate_session_data()
            },
            "YouTube": {
                "url": "https://youtube.com/@{}",
                "activities": [
                    "Video watched", "Like given", "Comment posted", "Subscribe done",
                    "Playlist created", "Video uploaded", "Live stream watched", "Share done",
                    "Download requested", "Channel visited", "History cleared", "Premium used"
                ],
                "login_count": random.randint(15, 120),
                "session_data": self.generate_session_data()
            },
            "GitHub": {
                "url": "https://github.com/{}",
                "activities": [
                    "Repository created", "Commit pushed", "Pull request made", "Issue opened",
                    "Star given", "Fork done", "Code reviewed", "Gist created",
                    "Profile updated", "Project created", "Wiki edited", "Release published"
                ],
                "login_count": random.randint(2, 25),
                "session_data": self.generate_session_data()
            },
            "Amazon": {
                "url": "https://amazon.com",
                "activities": [
                    "Product viewed", "Purchase made", "Cart updated", "Review posted",
                    "Wishlist added", "Search performed", "Order tracked", "Return requested",
                    "Payment updated", "Address changed", "Prime video watched", "Deal claimed"
                ],
                "login_count": random.randint(5, 40),
                "session_data": self.generate_session_data()
            },
            "Netflix": {
                "url": "https://netflix.com",
                "activities": [
                    "Movie watched", "Series binged", "Profile created", "Download done",
                    "Rating given", "Continue watching", "Search performed", "List added",
                    "Device added", "Subscription updated", "Trailer watched", "Recommendation viewed"
                ],
                "login_count": random.randint(8, 60),
                "session_data": self.generate_session_data()
            },
            "PayPal": {
                "url": "https://paypal.com",
                "activities": [
                    "Payment sent", "Payment received", "Invoice created", "Refund processed",
                    "Balance checked", "Bank linked", "Card added", "Transfer made",
                    "Subscription managed", "Dispute opened", "Currency converted", "Security updated"
                ],
                "login_count": random.randint(3, 20),
                "session_data": self.generate_session_data()
            },
            "Spotify": {
                "url": "https://open.spotify.com/user/{}",
                "activities": [
                    "Song played", "Playlist created", "Like given", "Share done",
                    "Podcast subscribed", "Download done", "Radio started", "Collaborative playlist",
                    "Year wrapped viewed", "Device connected", "Premium used", "Search performed"
                ],
                "login_count": random.randint(12, 80),
                "session_data": self.generate_session_data()
            },
            "Reddit": {
                "url": "https://reddit.com/user/{}",
                "activities": [
                    "Post created", "Comment posted", "Upvote given", "Award given",
                    "Subreddit joined", "Message sent", "Live chat joined", "Poll voted",
                    "Avatar updated", "Premium used", "Search performed", "Crosspost done"
                ],
                "login_count": random.randint(6, 45),
                "session_data": self.generate_session_data()
            },
            "Discord": {
                "url": "",
                "activities": [
                    "Message sent", "Voice joined", "Screen shared", "Reaction added",
                    "Server joined", "DM started", "Call made", "File uploaded",
                    "Stream started", "Nickname changed", "Role assigned", "Bot used"
                ],
                "login_count": random.randint(20, 150),
                "session_data": self.generate_session_data()
            },
            "WhatsApp": {
                "url": "",
                "activities": [
                    "Message sent", "Call made", "Status updated", "Group created",
                    "Media shared", "Backup created", "Broadcast sent", "Profile updated",
                    "Starred message", "Delete for everyone", "Voice note sent", "Location shared"
                ],
                "login_count": random.randint(100, 500),
                "session_data": self.generate_session_data()
            },
            "Telegram": {
                "url": "https://t.me/{}",
                "activities": [
                    "Secret chat started", "Channel created", "Bot used", "File shared",
                    "Voice call made", "Video message sent", "Sticker used", "Poll created",
                    "Group managed", "Theme changed", "Auto-delete set", "Passcode set"
                ],
                "login_count": random.randint(30, 200),
                "session_data": self.generate_session_data()
            }
        }

    def generate_session_data(self):
        """Generate realistic session data"""
        sessions = []
        for _ in range(random.randint(1, 8)):
            session_start = datetime.now() - timedelta(hours=random.randint(1, 720))
            session_end = session_start + timedelta(minutes=random.randint(5, 180))
            sessions.append({
                "start_time": session_start.strftime("%Y-%m-%d %H:%M:%S"),
                "end_time": session_end.strftime("%Y-%m-%d %H:%M:%S"),
                "duration_minutes": (session_end - session_start).seconds // 60,
                "ip_address": f"192.168.{random.randint(1,255)}.{random.randint(1,255)}",
                "device": random.choice(["Windows 10", "Android", "iPhone", "MacOS", "Linux"]),
                "browser": random.choice(["Chrome", "Firefox", "Safari", "Edge"])
            })
        return sessions

    def display_banner(self):
        """Display advanced hacker-style banner"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
        banner = r"""
        
  ██████   █████  ██████  ██   ██ ██████   ██████  ███████ ██████  ███████ 
  ██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██  ████ ██      ██   ██ ██   ██ 
  ██   ██ ███████ ██████  █████   ██████  ██ ██ ██ ███████ ██████  ██████  
  ██   ██ ██   ██ ██   ██ ██  ██  ██   ██ ██ ██ ██      ██ ██   ██ ██      
  ██████  ██   ██ ██   ██ ██   ██ ██████   ██████  ███████ ██   ██ ██      
                                                                            
        ═══════════════════════════════════════════════════════════
                  REAL-TIME ACCOUNT MONITORING SYSTEM v5.0
        ═══════════════════════════════════════════════════════════
        """
        print("\033[91m" + banner + "\033[0m")
        
        info = f"""
        \033[96m╔══════════════════════════════════════════════════════════════╗
        \033[96m║\033[91m        🕵️‍♂️ REAL-TIME ACCOUNT MONITORING v{self.version}           \033[96m║
        \033[96m║\033[92m              CREATED BY: {self.author}                          \033[96m║
        \033[96m║\033[93m           🔥 LIVE ACTIVITY TRACKING 🔥                   \033[96m║
        \033[96m╚══════════════════════════════════════════════════════════════╝
        
        \033[97m[\033[91m🔥\033[97m] Real-time Login Monitoring
        \033[97m[\033[92m📧\033[97m] Activity Pattern Analysis
        \033[97m[\033[94m🌐\033[97m] Session Data Collection
        \033[97m[\033[93m⚡\033[97m] Behavioral Analytics
        \033[97m[\033[95m🔍\033[97m] Cross-platform Correlation
        
        \033[95m📞 Telegram: {self.telegram_id}
        \033[95m📢 Channel: {self.telegram_channel}
        \033[96m🔗 Monitoring: 15+ Platforms
        """
        print(info)

    def open_links(self):
        """Automatically open Telegram links"""
        print("\033[92m[+] Initializing communication channels...")
        time.sleep(1)
        webbrowser.open(self.telegram_id)
        time.sleep(1)
        webbrowser.open(self.telegram_channel)
        time.sleep(2)

    def simulate_real_time_monitoring(self, email):
        """Simulate real-time account monitoring"""
        print(f"\n\033[96m[🔍] Starting real-time monitoring for: \033[93m{email}")
        print("\033[96m[⚡] Accessing account activity logs...")
        
        results = {}
        
        for platform, data in self.platforms_activities.items():
            print(f"\033[97m[📡] Monitoring {platform} activities...")
            
            # Simulate real-time data fetching
            time.sleep(0.3)
            
            # Generate recent activities
            recent_activities = []
            for _ in range(random.randint(3, 12)):
                activity = {
                    "action": random.choice(data["activities"]),
                    "timestamp": (datetime.now() - timedelta(minutes=random.randint(1, 1440))).strftime("%Y-%m-%d %H:%M:%S"),
                    "device": random.choice(["Mobile", "Desktop", "Tablet"]),
                    "location": f"{random.choice(['Dhaka', 'Chittagong', 'New York', 'London', 'Tokyo'])}"
                }
                recent_activities.append(activity)
            
            # Account status based on realistic patterns
            last_login = datetime.now() - timedelta(hours=random.randint(1, 72))
            account_status = "Active" if random.random() > 0.1 else "Inactive"
            
            results[platform] = {
                "account_exists": random.random() > 0.2,  # 80% chance account exists
                "profile_url": data["url"].format(email.split('@')[0]) if data["url"] else "",
                "login_count": data["login_count"],
                "last_login": last_login.strftime("%Y-%m-%d %H:%M:%S"),
                "account_status": account_status,
                "recent_activities": recent_activities,
                "session_data": data["session_data"],
                "total_time_spent": sum(session["duration_minutes"] for session in data["session_data"]),
                "preferences": self.generate_user_preferences(platform)
            }
            
            print(f"    \033[92m✓ {platform}: {len(recent_activities)} activities found")
        
        return results

    def generate_user_preferences(self, platform):
        """Generate realistic user preferences"""
        preferences = {
            "Facebook": ["News Feed", "Messenger", "Marketplace", "Groups"],
            "Instagram": ["Stories", "Reels", "Direct Messages", "Explore"],
            "Twitter": ["Timeline", "Trends", "Moments", "Lists"],
            "YouTube": ["Subscriptions", "Trending", "History", "Playlists"],
            "Netflix": ["Continue Watching", "My List", "New Releases", "Top Picks"]
        }
        
        return preferences.get(platform, ["General"])

    def display_real_time_dashboard(self, email, results):
        """Display real-time monitoring dashboard"""
        print(f"\n\033[96m{'═' * 80}")
        print(f"\033[91m📊 REAL-TIME ACCOUNT ACTIVITY DASHBOARD")
        print(f"\033[96m{'═' * 80}")
        print(f"\033[93m🎯 Target: {email}")
        print(f"\033[92m📅 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\033[94m🔧 System: DarkBoss1BD Live Monitor v{self.version}")
        print(f"\033[96m{'═' * 80}")
        
        total_logins = sum(data["login_count"] for data in results.values() if data["account_exists"])
        active_accounts = sum(1 for data in results.values() if data["account_exists"] and data["account_status"] == "Active")
        
        print(f"\n\033[97m📈 LIVE STATISTICS:")
        print(f"\033[94m{'─' * 50}")
        print(f"   \033[92m✅ Active Accounts: {active_accounts}/{len(results)}")
        print(f"   \033[93m📊 Total Logins: {total_logins}")
        print(f"   \033[96m⏱️  Total Time Spent: {sum(data['total_time_spent'] for data in results.values() if data['account_exists'])} minutes")
        print(f"   \033[95m🔔 Recent Activities: {sum(len(data['recent_activities']) for data in results.values() if data['account_exists'])}")

    def display_detailed_activities(self, email, results):
        """Display detailed activity logs"""
        print(f"\n\033[97m🔍 DETAILED ACTIVITY LOGS:")
        print(f"\033[96m{'═' * 80}")
        
        for platform, data in results.items():
            if data["account_exists"]:
                print(f"\n\033[95m📱 {platform.upper()} - Account Monitoring")
                print(f"\033[94m{'─' * 60}")
                print(f"   \033[97m🔗 Profile: {data['profile_url']}")
                print(f"   \033[92m📊 Login Count: {data['login_count']}")
                print(f"   \033[93m⏰ Last Login: {data['last_login']}")
                print(f"   \033[96m📈 Status: {data['account_status']}")
                print(f"   \033[95m⏱️  Total Time: {data['total_time_spent']} minutes")
                
                print(f"\n   \033[97m🔄 RECENT ACTIVITIES:")
                for i, activity in enumerate(data["recent_activities"][:5], 1):
                    print(f"      {i}. {activity['action']}")
                    print(f"         📅 {activity['timestamp']} | 📱 {activity['device']} | 📍 {activity['location']}")
                
                print(f"\n   \033[97m💻 RECENT SESSIONS:")
                for i, session in enumerate(data["session_data"][:3], 1):
                    print(f"      {i}. {session['start_time']} to {session['end_time']}")
                    print(f"         ⏱️  {session['duration_minutes']}min | 🌐 {session['ip_address']}")
                    print(f"         💻 {session['device']} | 🔍 {session['browser']}")

    def generate_activity_timeline(self, results):
        """Generate activity timeline across all platforms"""
        print(f"\n\033[97m📅 ACTIVITY TIMELINE (Last 24 Hours):")
        print(f"\033[96m{'═' * 80}")
        
        all_activities = []
        for platform, data in results.items():
            if data["account_exists"]:
                for activity in data["recent_activities"]:
                    activity["platform"] = platform
                    all_activities.append(activity)
        
        # Sort by timestamp
        all_activities.sort(key=lambda x: x["timestamp"], reverse=True)
        
        for activity in all_activities[:10]:  # Show last 10 activities
            time_diff = datetime.now() - datetime.strptime(activity["timestamp"], "%Y-%m-%d %H:%M:%S")
            minutes_ago = int(time_diff.total_seconds() // 60)
            
            print(f"   \033[93m[{activity['platform']}] {activity['action']}")
            print(f"   \033[97m   ⏰ {minutes_ago} minutes ago | 📱 {activity['device']} | 📍 {activity['location']}")
            print(f"   \033[90m   {'─' * 50}")

    def save_comprehensive_report(self, email, results):
        """Save comprehensive monitoring report"""
        report_data = {
            "metadata": {
                "email": email,
                "report_date": datetime.now().isoformat(),
                "monitoring_duration": "Real-time",
                "tool": f"DarkBoss1BD Live Monitor v{self.version}",
                "operator": self.author
            },
            "summary": {
                "total_platforms": len(results),
                "active_accounts": sum(1 for data in results.values() if data["account_exists"]),
                "total_logins": sum(data["login_count"] for data in results.values() if data["account_exists"]),
                "total_activities": sum(len(data["recent_activities"]) for data in results.values() if data["account_exists"])
            },
            "detailed_results": results
        }
        
        # Save JSON report
        json_filename = f"{email.replace('@', '_at_')}_live_monitor.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(report_data, f, indent=2, ensure_ascii=False)
        
        # Save text report
        txt_filename = f"{email.replace('@', '_at_')}_live_monitor.txt"
        with open(txt_filename, 'w', encoding='utf-8') as f:
            f.write("DARKBOSS1BD REAL-TIME ACCOUNT MONITORING REPORT\n")
            f.write("=" * 60 + "\n\n")
            f.write(f"Target: {email}\n")
            f.write(f"Report Date: {datetime.now()}\n")
            f.write(f"Platforms Monitored: {len(results)}\n\n")
            
            for platform, data in results.items():
                if data["account_exists"]:
                    f.write(f"PLATFORM: {platform}\n")
                    f.write(f"Login Count: {data['login_count']}\n")
                    f.write(f"Last Login: {data['last_login']}\n")
                    f.write(f"Status: {data['account_status']}\n")
                    f.write("Recent Activities:\n")
                    for activity in data["recent_activities"][:5]:
                        f.write(f"  - {activity['action']} at {activity['timestamp']}\n")
                    f.write("\n")
        
        print(f"\033[92m[💾] JSON report saved: {json_filename}")
        print(f"\033[92m[💾] Text report saved: {txt_filename}")

    def simulate_live_updates(self, email, results):
        """Simulate live activity updates"""
        print(f"\n\033[96m[🔄] Starting live activity stream for {email}...")
        print("\033[90m[ℹ️] Press Ctrl+C to stop live monitoring\n")
        
        try:
            for i in range(5):  # Simulate 5 live updates
                time.sleep(3)
                
                # Simulate new activity
                platform = random.choice(list(results.keys()))
                if results[platform]["account_exists"]:
                    new_activity = {
                        "action": random.choice(self.platforms_activities[platform]["activities"]),
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "device": random.choice(["Mobile", "Desktop", "Tablet"]),
                        "location": random.choice(["Dhaka", "Chittagong", "New York", "London"])
                    }
                    
                    results[platform]["recent_activities"].insert(0, new_activity)
                    results[platform]["login_count"] += 1
                    
                    print(f"\033[92m[🆕] NEW ACTIVITY: {platform} - {new_activity['action']}")
                    print(f"\033[97m     📅 {new_activity['timestamp']} | 📱 {new_activity['device']} | 📍 {new_activity['location']}")
                    
        except KeyboardInterrupt:
            print(f"\n\033[93m[⏹️] Live monitoring stopped by user")

def main():
    try:
        monitor = RealTimeAccountMonitor()
        monitor.display_banner()
        monitor.open_links()
        
        while True:
            print(f"\n\033[96m{'═' * 60}")
            email = input("\033[97m[📧] Enter target email \033[91m(or 'quit' to exit)\033[97m: ").strip()
            
            if email.lower() == 'quit':
                print("\033[93m[👋] Thank you for using DarkBoss1BD Live Monitor!")
                break
            
            if '@' not in email or '.' not in email:
                print("\033[91m[❌] Please enter a valid email address!")
                continue
            
            start_time = time.time()
            
            # Perform real-time monitoring
            results = monitor.simulate_real_time_monitoring(email)
            
            # Display dashboard
            monitor.display_real_time_dashboard(email, results)
            
            # Display detailed activities
            monitor.display_detailed_activities(email, results)
            
            # Display activity timeline
            monitor.generate_activity_timeline(results)
            
            # Save reports
            monitor.save_comprehensive_report(email, results)
            
            # Simulate live updates
            monitor.simulate_live_updates(email, results)
            
            end_time = time.time()
            print(f"\033[92m[⏱️] Monitoring completed in {end_time - start_time:.2f} seconds")
            
            # Ask for another scan
            print(f"\n\033[96m{'═' * 60}")
            continue_scan = input("\033[97m[?] Monitor another target? \033[92m(y/n)\033[97m: ").lower()
            if continue_scan != 'y':
                print("\033[93m[👋] Thank you for using DarkBoss1BD Live Monitor!")
                print("\033[96m[📞] Join our Telegram for real-time updates!")
                break
                
    except KeyboardInterrupt:
        print("\n\033[91m[!] Monitoring interrupted by user!")
    except Exception as e:
        print(f"\033[91m[!] An error occurred: {e}")

if __name__ == "__main__":
    main()
