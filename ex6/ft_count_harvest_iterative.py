# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_iterative.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 23:09:22 by mgerard           #+#    #+#              #
#    Updated: 2026/05/08 23:32:13 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_iterative():
    days = input("Days until harvest: ")
    limits = range(1, int(days) + 1)
    for nb in limits:
        print(f"Day {nb}")
    print("Harvest time!")
