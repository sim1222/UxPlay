/**
 *  Copyright (C) 2011-2012  Juho Vähä-Herttua
 *
 *  This library is free software; you can redistribute it and/or
 *  modify it under the terms of the GNU Lesser General Public
 *  License as published by the Free Software Foundation; either
 *  version 2.1 of the License, or (at your option) any later version.
 *
 *  This library is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  Lesser General Public License for more details.
 *
 *==================================================================
 * modified by fduncanh 2021-2022
 */

#ifndef UTILS_H
#define UTILS_H

#include <stdint.h>

char *utils_strsep(char **stringp, const char *delim);
int utils_read_file(char **dst, const char *pemstr);
int utils_hwaddr_raop(char *str, int strlen, const char *hwaddr, int hwaddrlen);
int utils_hwaddr_airplay(char *str, int strlen, const char *hwaddr, int hwaddrlen);
char *utils_parse_hex(const char *str, int str_len, int *data_len);
char *utils_data_to_string(const unsigned char *data, int datalen, int chars_per_line);
char *utils_data_to_text(const char *data, int datalen);
void ntp_timestamp_to_time(uint64_t ntp_timestamp, char *timestamp, size_t maxsize);
void ntp_timestamp_to_seconds(uint64_t ntp_timestamp, char *timestamp, size_t maxsize);
#endif
