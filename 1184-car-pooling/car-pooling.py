class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Find the maximum drop-off location to size the timeline array
        max_location = max(trip[2] for trip in trips)
        
        # Initialize the timeline array with zeros
        timeline = [0] * (max_location + 1)
        
        # Update the timeline for each trip
        for num_passengers, from_loc, to_loc in trips:
            timeline[from_loc] += num_passengers
            if to_loc < len(timeline):
                timeline[to_loc] -= num_passengers
        
        # Calculate the prefix sum and check the capacity
        current_passengers = 0
        for passengers in timeline:
            current_passengers += passengers
            if current_passengers > capacity:
                return False
        
        return True


