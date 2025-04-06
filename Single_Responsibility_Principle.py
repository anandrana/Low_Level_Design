# Class responsible for holding and formatting report data
class Report:
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def get_report(self):
        return f"=== {self.title} ===\n{self.content}"


# Class responsible for saving report data
class ReportSaver:
    def save_to_file(self, report, filename):
        with open(filename, 'w') as file:
            file.write(report.get_report())
        print(f"Report saved to {filename}")


# Class responsible for sending report via email (Another responsibility separated)
class ReportEmailer:
    def send_email(self, report, to_email):
        print(f"Sending report to {to_email}...")
        # Simulate sending email
        print(f"Email sent with content:\n\n{report.get_report()}")


# --- Using the above classes ---

if __name__ == "__main__":
    report = Report("Weekly Summary", "Everything went well this week. All goals met.")
    
    saver = ReportSaver()
    saver.save_to_file(report, "weekly_report.txt")
    
    emailer = ReportEmailer()
    emailer.send_email(report, "team@example.com")
