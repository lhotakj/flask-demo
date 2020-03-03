from flask import make_response, jsonify

from app.config import Configuration


class ApiAwsController:
    config = Configuration.Configuration()

    def __init__(self):
        pass

    def action_ec2(self, action):
        return make_response(jsonify(
            {}
        ), 200, {"content_type": "application/json"})

    def list_ec2_tags(self, tags):
        # self.config.logger().info(request.method + " " + request.url)
        return make_response(jsonify(
            {
                "data": [
                    {
                        "name": "devel",
                        "instance_id": "id-115654477",
                        "ami_id": "ami-56446487879",
                        "owner": "za577",
                        "cpu": "6c/2h",
                        "status": "running",
                    },
                    {
                        "name": "compilation-009.300.000",
                        "instance_id": "id-81565447a",
                        "ami_id": "ami-56446487879",
                        "owner": "rint",
                        "cpu": "6c/2h",
                        "status": "stopped",
                    },
                    {
                        "name": "compilation-009.300.001",
                        "instance_id": "id-81565447a",
                        "ami_id": "ami-56446487879",
                        "owner": "rint",
                        "cpu": "6c/2h",
                        "status": "running",
                    }
                ]
            }
        ), 200, {"content_type": "application/json"})


api_aws_controller = ApiAwsController()
