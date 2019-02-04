from googleapiclient import discovery
from pprint import pprint
from oauth2client.client import GoogleCredentials
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file('C:\GIT Local Repo\Keys\crucial-inn-228012-be47e54fcf62.json')  

def getOrgName():
    service = discovery.build('cloudresourcemanager', 'v1beta1', credentials=credentials)
    request = service.organizations().list()

    if request is not None:
        response = request.execute()
        for organization in response['organizations']:
            org_name = organization['displayName']
    return org_name


def getOrgId():
    service = discovery.build('cloudresourcemanager', 'v1beta1', credentials=credentials)
    request = service.organizations().list()

    if request is not None:
        response = request.execute()
        for organization in response['organizations']:
            org_id = organization['organizationId']

    return org_id

def ListInstances():
        instance_list = []
        compute = discovery.build('compute', 'v1', credentials=credentials)
        resource_manager = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)
        resource_manager_request = resource_manager.projects().list()
        if resource_manager_request is not None:
            resource_manager_response = resource_manager_request.execute()
            #print(resource_manager_response)
            for project in resource_manager_response['projects']:
                #print("In project '%s', you have below mentioned instances:" %(project['name']))
                zone_request = compute.zones().list(project=project['projectId'])
                if zone_request is not None:
                    try:
                        zone_response = zone_request.execute()
                        for zone in zone_response['items']:
                            compute_request = compute.instances().list(project=project['projectId'], zone=zone['name'])
                            #pprint(compute_request)
                            if compute_request is not None:
                                compute_response = compute_request.execute()
                                #pprint(compute_response['items'])
                                for instance in compute_response['items']:
                                    instance_list.append(instance['name'])
                    except Exception as e:
                        pass
                else:
                    print('0 Instances')
        return instance_list
