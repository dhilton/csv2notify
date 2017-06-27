from notifications_python_client.notifications import NotificationsAPIClient
import click
import os
import sys
import csv
from urllib.error import HTTPError


# cli-fae7bf3c-596c-45d6-b31e-04d1b411ee86-35faf6d0-26cd-4fa8-b5a7-9c44f492f43b

try:
    API_KEY = os.environ["NOTIFY_API_KEY"]
    notifications_client = NotificationsAPIClient(API_KEY)
except KeyError:
    print("Please set the environment variable NOTIFY_API_KEY with your API key from https://www.notifications.service.gov.uk/")
    sys.exit(1)


@click.command()
@click.option('--check', '-c', is_flag=True, help='Check a if a csv file is valid, containing no issues')
@click.option('--email-field', help='The header of the column containing an entry\'s email address')
@click.option('--mobile-field', help='The header of the column containing mobile numbers')
@click.option('--template-id', help='The ID of the template you wish to use')
@click.argument('csv_file', required=True)
def main(csv_file, check, email_field=None, mobile_field=None, template_id=None):
    """Stream a CSV file to GOV.UK Notify API

    Given a single CSV file, go through each line sending a notification for
    each entry.
    """
    with open(csv_file, newline='') as csvfile:
        notifyreader = csv.DictReader(csvfile)
        for row in notifyreader:
            if email_field and template_id:
                print("Sending email to {}".format(row[email_field]))
                try:
                    response = notifications_client.send_email_notification(
                        email_address=row[email_field],
                        template_id=template_id,
                        personalisation=row,
                        reference=None
                    )
                    print("5x5 we're in the pipe")
                except HTTPError as e:
                    print("Oops! Error is: {}".format(e.message))
            elif mobile_field:
                print(row[mobile_field])
            else:
                print('Error: no mobile or email field given.')
                return


if __name__ == '__main__':
    main()
