
import os
import ansible_runner
import boto3

def read_from_sqs_queue():
    #queue_url = os.environ["sqs_queue_url"]
    queue_url = "https://sqs.eu-west-1.amazonaws.com/532272748741/GitOps"
    sqs_client = boto3.client(
        "sqs",
        region_name="eu-west-1",
    )

    response = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        WaitTimeSeconds=20
    )

    if not response.get('Messages'):
        return None

    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    
    print(message)

    # Delete received message from queue
    sqs_client.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=receipt_handle
    )


    return message


def update_blue():
    r = ansible_runner.run(private_data_dir='../docker-manager', playbook='update-blue.yml')
    print("{}: {}".format(r.status, r.rc))
    # successful: 0
    for each_host_event in r.events:
        print(each_host_event['event'])
    print("Final status:")
    print(r.stats)

while True:
    print(".")
    read_from_sqs_queue()



