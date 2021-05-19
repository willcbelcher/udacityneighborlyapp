import json
import logging
import azure.functions as func


def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

	# logging.info('Function triggered to process a message: ', event.get_body())
    # logging.info('  EnqueuedTimeUtc =', event.enqueued_time)
    # logging.info('  SequenceNumber =', event.sequence_number)
    # logging.info('  Offset =', event.offset)

    # result = json.dumps({
    #     'id': event.id,
    #     'data': event.get_json(),
    #     'topic': event.topic,
    #     'subject': event.subject,
    #     'event_type': event.event_type,
    # })

    value = "Sending message from my Azure Functions HTTP Trigger"

    message = {
        "personalizations": [ {
          "to": [{
            "email": "williambelcher2020@u.northwestern.edu"
            }]}],
        "subject": "[AZURE FUNCTIONS SENDGRID] email",
        "content": [{
            "type": "text/plain",
            "value": value }]}

    sendGridMessage.set(json.dumps(message))
    # logging.info('Python EventGrid trigger processed an event: %s', result)
    return func.HttpResponse("Message successfully sent.")


    



