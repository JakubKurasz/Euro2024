from statsbombpy import sb

class DataCollector:
    """
    This class is used to gather data from the statsbomb
    open source api
    """

    @staticmethod
    def choose_match(id, team, event_type):
        """
        This method takes in a match id, team, and event type and returns the corresponding events
        """
        events = sb.events(match_id=id)
        events = events[events['team'] == team]
        events = events[events['type']==event_type]
        return events
    
    @staticmethod
    def collect_data(events):
        """
        This method parses events data and returns several more digestible arrays
        """
        location= []
        end = []
        minutes = []
        outcome = []
        for event in events['pass_outcome']:
            outcome.append(event)
        for event in events['location']:
            location.append(event)
        for event in events['pass_end_location']:
            end.append(event)
        for event in events['minute']:
            minutes.append(event)
        return outcome, location, end, minutes