from drf_yasg import openapi

response_schema_dict_create_events = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "id": 1,
                "sensor_id": 1,
                "name": "some_name",
                "temperature": 20,
                "humidity": 30
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "non_field_errors": [
                    "Expected a list of items but got type \"dict\"."
                ],
                "sensor_id": [
                    "Invalid pk \"0\" - object does not exist."
                ],
                "sensor_id_required": [
                    "This field is required."
                ],
                "name": [
                    "This field is required."
                ]

            }
        }
    ),
}

response_schema_dict_create_sensors = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "name": "some_name",
                "type": 1
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "non_field_errors": [
                    "Expected a list of items but got type \"dict\"."
                ],
                "name": [
                    "This field is required."
                ],
                "type": [
                    "This field is required."
                ],

            }
        }
    ),
}

response_schema_dict_update_events = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "id": 1,
                "sensor_id": 1,
                "name": "some_name",
                "temperature": 20,
                "humidity": 30
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "non_field_errors": [
                    "Invalid data. Expected a dictionary, but got list."
                ],
                "sensor_id_required": [
                    "This field is required."
                ],
                "name": [
                    "This field is required."
                ],
                "400": "Event does not exist"
            }
        }
    ),
}

response_schema_dict_update_sensors = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "name": "some_name",
                "type": 1
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "non_field_errors": [
                    "Invalid data. Expected a dictionary, but got list."
                ],
                "name": [
                    "This field is required."
                ],
                "type": [
                    "This field is required."
                ],
                "400": "Sensor does not exist"

            }
        }
    ),
}

response_schema_dict_delete_sensors = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "200":"Sensor id = 1 was deleted"
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "400": "Sensor does not exist",
            }
        }
    ),
}

response_schema_dict_delete_events = {
    "200": openapi.Response(
        description="200",
        examples={
            "application/json": {
                "200":"Event id = 1 was deleted"
            }
        }
    ),
    "400": openapi.Response(
        description="custom 400 description",
        examples={
            "application/json": {
                "400": "Event does not exist",
            }
        }
    ),
}
