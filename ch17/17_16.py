# Cracking the Coding Interview: 17.16
# Written by Josh Humphrey

bookings = [30,15,60,75,45,15,15,45]

def best_booking(bookings, index):
    if index >= len(bookings):
        return 0

    take_next = best_booking(bookings, index + 1)
    skip_next = bookings[index] + best_booking(bookings, index + 2)
    result = max(take_next, skip_next)
    return result

result = best_booking(bookings, 0)
print("Maximum Number of Minutes: " + str(result))
