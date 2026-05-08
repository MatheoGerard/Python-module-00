# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_harvest_total.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mgerard <mgerard@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/05/08 21:09:55 by mgerard           #+#    #+#              #
#    Updated: 2026/05/08 21:16:21 by mgerard          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_harvest_total():
    day1 = input("Day 1 harvest: ")
    day2 = input("Day 2 harvest: ")
    day3 = input("Day 3 harvest: ")
    print(f"Total harvest: {int(day1) + int(day2) + int(day3)}")
