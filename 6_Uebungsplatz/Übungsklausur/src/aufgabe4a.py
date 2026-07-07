def berechne_ticketpreis(alter):
    if alter < 0:
        return "Ungültiges Alter"
    elif alter <= 12:
        return 5.0
    elif alter <= 65:
        return 10.0
    else:
        return 7.5