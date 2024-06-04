# Mail Sending Application

This application reads a CSV file containing names and email addresses, generates personalized email bodies using a template, and sends the emails via Gmail.

## Features
- Read contacts from a CSV file
- Personalize email content with names
- Send emails using Gmail SMTP

## Prerequisites
- Python 3.x
- `smtplib` library (built-in)
- `csv` library (built-in)
- Gmail account for sending emails

## How to Use It

1. **Clone or Download the Repository**:
    ```sh
    git clone https://github.com/yourusername/mail-sending-application.git
    ```

2. **Navigate to the Application Directory**:
    - Start WSL or open a Linux terminal.
    - Change directory to the application folder within the cloned repository:
      ```sh
      cd mail-sending-application
      ```

3. **Prepare Your Data**:
    - Ensure you have a `contacts.csv` file in the `data` folder with the following format:
      ```csv
      John Doe,john.doe@example.com
      Jane Smith,jane.smith@example.com
      ```
    - Create an `email_template.txt` file in the `data` folder with your email template, including the `<NAME>` placeholder:
      ```txt
      Dear <NAME>,

      I would like to apply to the open job position at your company.

      Sincerely,
      Rob
      ```

4. **Run the Script**:
    ```sh
    python3 main.py
    ```
    The script will read the CSV file and the email template, then prompt you for your Gmail email address and password. It will display the generated email text and ask if you want to send each email.

## Security Considerations
- This script will prompt for your Gmail password. For security, consider using an app-specific password if you have 2FA enabled. You can generate an app-specific password by following [Google's instructions](https://support.google.com/mail/answer/185833).

## License
This project is licensed under the GPL 3.0 License - see the LICENSE file for details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request.

## Acknowledgements
- [smtplib](https://docs.python.org/3/library/smtplib.html): Python library for sending emails
- [csv](https://docs.python.org/3/library/csv.html): Python library for reading and writing CSV files
