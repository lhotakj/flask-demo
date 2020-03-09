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

    def cloud_watch_tags(self, tags, duration):

        if duration == "8h":
            return make_response(jsonify(
                {
                    "data": [
                        {
                            "instance_id": "i-5454455ab",
                            "labels": ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00'],
                            "memory": [3, 9, 10, 8, 10, 9, 3, 5],
                            "cpu": [70, 20, 50, 87, 98, 99, 66, 68],
                            "swap": [21, 20, 10, 1, 20, 18, 13, 12]
                        }
                    ]
                }
            ), 200, {"content_type": "application/json"})

        if duration == "24h":
            return make_response(jsonify(
                {
                    "data": [
                        {
                            "instance_id": "i-5454455ab",
                            "labels": ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00',
                                       '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
                                       '18:00', '19:00', '20:00', '21:00', '22:00', '23:00', '24:00'],
                            "memory": [12, 6, 3, 6, 10, 16, 20, 22, 23, 50, 55, 20, 21, 23, 18, 87, 80, 21, 93, 18, 17,
                                       16,
                                       15, 13, 12],
                            "cpu": [90, 20, 50, 1, 98, 99, 96, 99, 99, 99, 100, 96, 99, 99, 99, 100, 96, 99, 99, 99,
                                    100,
                                    100, 100, 99, 98],
                            "swap": [21, 20, 10, 1, 20, 18, 13, 12, 15, 16, 19, 20, 19, 20, 23, 22, 13, 12, 15, 26, 19,
                                     19,
                                     16, 20, 20]
                        }
                    ]
                }
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
