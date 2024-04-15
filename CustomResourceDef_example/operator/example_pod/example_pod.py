import logging
from kubernetes import client, config, watch

# Configure logging
logging.basicConfig(level=logging.INFO)

def process_myresource_event(event):
    resource = event['object']
    if event['type'] == 'ADDED':
        print(f"New MyResource added: {resource['metadata']['name']}")
        logging.info(f"New MyResource added: {resource['metadata']['name']}")
        # Add your custom logic here to handle the new resource
    elif event['type'] == 'DELETED':
        print(f"MyResource deleted: {resource['metadata']['name']}")
        logging.info(f"MyResource deleted: {resource['metadata']['name']}")
        # Add your custom logic here to handle the deleted resource

def main():
    config.load_incluster_config()  # Load in-cluster Kubernetes configuration
    api_instance = client.CustomObjectsApi()

    print(api_instance)
    logging.info(api_instance)
    resource_version = ''
    while True:
        stream = watch.Watch().stream(api_instance.list_cluster_custom_object,
                                       "example.io", "v1", "greetings", resource_version=resource_version)

        for event in stream:
            process_myresource_event(event)
            resource_version = event['object']['metadata'].get('resourceVersion')

if __name__ == '__main__':
    main()