from flask.ext.restful import marshal, request

from humanoid.joints import HingeJoint


class Knee(HingeJoint):
    """
    Knee extends the basic hinge joint class and
    sets a limit to its own movement.
    """

    def __init__(self):
        super(Knee, self).__init__()

        # Number of degrees that the joint is limited to.
        self.data["limits"] = [0, 50]

        self.parent_id = None

        self.data["href"] = "/api/robot/body/legs/" + str(self.parent_id) + "/knee/"

    def set_parent_id(self, uuid):
        self.parent_id = uuid
        self.data["href"] = "/api/robot/body/legs/" + str(uuid) + "/knee/"

    def get(self, leg_id):
        self.data["href"] = "/api/robot/body/legs/" + str(leg_id) + "/knee/"
        # TODO: Create arm and leg representation in database,
        # An error will be thrown if the arm or leg does not exist in the db.

        return marshal(self.data, self.fields)

    def patch(self, leg_id):
        data = request.get_json(force=True)

        self.validate_fields(data)

        for key in data.keys():
            self.data[key] = data[key]

        return marshal(self.data, self.fields), 201