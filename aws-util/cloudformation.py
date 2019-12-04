import boto3

'''
waiter options:
'stack_create_complete'
'change_set_create_complete'
'stack_delete_complete'
'stack_exists'
'stack_update_complete'
'''


def wait_for_stack(stack_name, waiter_option):
    client = boto3.client('cloudformation')
    waiter = client.get_waiter(waiter_option)
    waiter.wait(
        StackName=stack_name,
        WaiterConfig={
            'Delay': 10,
            'MaxAttempts': 1000
        }
    )


def create_stack(configs, delete_if_present=False, wait_for_create=True):
    # create a new stack
    client = boto3.client('cloudformation')

    if delete_if_present:
        client.delete_stack(configs['StackName'])
        wait_for_stack(configs['StackName'], 'stack_delete_complete')

    client.create_stack(**configs)

    if wait_for_create:
        wait_for_stack(configs['StackName'], 'stack_create_complete')
