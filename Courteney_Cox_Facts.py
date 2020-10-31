# -*- coding: utf-8 -*-

# This sample demonstrates handling intents from an Alexa skill using the Alexa Skills Kit SDK for Python.
# Please visit https://alexa.design/cookbook for additional examples on implementing slots, dialog management,
# session persistence, api calls, and more.
# This sample is built using the handler classes approach in skill builder.
import logging
import ask_sdk_core.utils as ask_utils

import random 

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


facts = ['Cox was born and raised in Mountain Brook, Alabama, a suburb of Birmingham.',
         'She is best identified for her roles as Monica Geller on the NBC sitcom Friends, Gale Weathers in the horror series Scream, and as Jules Cobb in the ABC/TBS sitcom Cougar Town, for which she earned her first Golden Globe nomination.',
         'Courteney attended Mountain Brook High School in Alabama.',
         ' In 1997, Courteney was voted Best Dressed Female Television Star.',
         'Courteney can play the drums and the piano.',
         'Even before they became a couple on the show, Cox said that if Monica had to “do” a Friend, she would choose Chandler. In the Elle profile from 1997, Cox was asked “if Monica had to ‘do’ another Friend, which would it be?” Her answer? “Chandler,” because in her mind, the character’s sarcastic bite was similar to Monica’s. The two characters eventually hooked up during the Season 4 finale in London, almost exactly a year after the quote was published.',
         'Courteney’s first ever movie was Masters of the Universe in 1987.',
         'Cox was a neat freak just like Monica and would clean the others’ dressing rooms. “Let’s face it, she’s adorable and intelligent and really together. She is Monica,” show co-creator Marta Kauffman told the Los Angeles Times in 1995. “She has the neatest dressing room. She even cleans up the other actors’ dressing rooms because she won’t go in there if they are too messy.”',
         'Courteney appeared in two of NBC’s public service announcements, The More You Know. Her topics were violence prevention and designated drivers.',
         'Cox also starred in the FX series Dirt.',
         'Cox also starred in the FX series Dirt.',
         'Courteney was pregnant during the filming of the final season of Friends.',
         'Courteney has brown hair and blue eyes.',
         'During her senior year, Courteney got her first modeling gig in an advertisement for a store called Parisians.',
         'Courteney received $32,300 of bed linen as a housewarming gift from Jennifer Aniston.',
         'Courteney was in all three Scream movies playing news reporter, Gale Weathers.',
         'She owns a production company, called Coquette Productions, which was created by her and her then-husband David Arquette.',
         'Courteney raises awareness for the skin disease epidomolysis bullosa. She has designed an eye shadow palette — Coco for Cargo Cosmetics. All profits will go to research, and hopefully find prevention for this disease.',
         'Cox also worked as a director on her sitcom Cougar Town and the television movie Talhotblond.',
         'Courteney bought the moving bookcase which appears in the movie Scream 3.',
         'Courteney’s nickname is CeCe.',
         'She has two older sisters, Virginia and Dottie, and an older brother, Richard, Jr.',
         'Courteney’s height is 5’5″.',
         'Courteney’s parents are Richard and Courteney Cox. She has two older sisters, Virginia and Dottie, and an older brother Richard.',
         'On Friends, Courteney was originally cast the part of ‘Rachel Green’ but the writers and producers thought the part of ‘Monica Gellar’ would suit her better.',
         'Courteney’s daughter’s godmother is Friends co-star Jennifer Aniston.',
         'Her parents divorced in 1974 and her mother then married businessman Hunter Copeland (uncle to music promoter and business manager Ian Copeland).',
         'Courteney shared a Screen Actors Guild award with the rest of the cast of Friends for Outstanding Ensemble Performance in a Comedy series in 1996. They were nominated six straight years from 1999-2004, all without a win.',
         'In different years, Courteney was married on June 12, gave birth on June 13, and born on June 15.',
         'Courteney was the best known cast member of the hit TV show Friends when it began its 10 year run.',
         'After graduating from Mountain Brook High School, Cox left for Mount Vernon College in Washington, D.C., but did not complete her architecture course, opting instead to pursue a career in modeling and acting.',
         'Despite the fact that she’s the only cast member of Friends without an Emmy nomination, Courteney has had four box office hits: the trilogy Scream and the 1994 film Ace Ventura.',
         'In 1997 and 1998 she was listed at number 9 in FHM’s 100 sexiest women list (readers’ choice).',
         'After graduating from Mountain Brook High School, Cox left for Mount Vernon College in Washington, D.C., but did not complete her architecture course, opting instead to pursue a career in modeling and acting.',
         'Courteney announced her pregnancy in January 2004, two months after David Arquette’s brother Alexis broke the news on The Sharon Osbourne Show. The couple wanted to keep the news quiet because Courteney had several miscarriages.',
         'Courteney’s daughter’s name is Coco Riley Arquette.',
         'She identifies as Irish-American.',
         'Courteney had laser eye surgery.',
         'As a child, she was an avid swimmer and tennis player.']

class FactIntenthandler(AbstractRequestHandler):
    
    def can_handle(self,handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input) or ask_utils.is_intent_name("FactIntent")(handler_input)
    
    def handle(self,handler_input):
        speak_output = random.choice(facts)
        return(
            handler_input.response_builder
            .speak(speak_output)
            .ask(speak_output)
            .response
            )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I had trouble doing what you asked. Please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = SkillBuilder()
sb.add_request_handler(FactIntenthandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()