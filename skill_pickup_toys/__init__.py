# TODO: Add an appropriate license to your skill before publishing.  See
# the LICENSE file for more information.

# Below is the list of outside modules you'll be using in your skill.
# They might be built-in to Python, from mycroft-core or from external
# libraries.  If you use an external library, be sure to include it
# in the requirements.txt file so the library is installed properly
# when the skill gets installed later by a user.

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from mycroft import intent_handler
import rospy
from std_msgs.msg import String

__author__ = 'fxgovers'

LOGGER = getLogger(__name__)
pub = rospy.Publisher('/syscommand', String, queue_size=1000)

def pubMessage(str):
	pub.publish(str)


class CleanRoomSkill(MycroftSkill):
    def __init__(self):
        super(CleanRoomSkill, self).__init__(name="CleanRoomSkill")

    def initialize(self):
        clean_room_intent = IntentBuilder("CleanRoomIntent"). \
            require("CleanRoomKeyword").build()
        self.register_intent(clean_room_intent, self.handle_clean_room_intent)



    def handle_clean_room_intent(self, message):
        self.speak_dialog("clean.up.room")
		pubMessage("PICK_UP_TOYS")

    def stop(self):
        pass


def create_skill():
    return CleanRoomSkill()

