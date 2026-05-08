# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_seed_inventory.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/09 00:23:02 by mgerard           #+#    #+#              #
#    Updated: 2026/05/09 00:46:58 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed_type = seed_type.capitalize()
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{seed_type} seeds: covers {quantity} {unit} square meters")
    else:
        print(f"{seed_type} seeds: {quantity} {unit} Unknown unit type")
