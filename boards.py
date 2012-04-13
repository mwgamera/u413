'''u413 - an open-source BBS/terminal/PI-themed forum
	Copyright (C) 2012 PiMaster
	Copyright (C) 2012 EnKrypt

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU Affero General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU Affero General Public License for more details.

	You should have received a copy of the GNU Affero General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.'''

import command
import display
import database

def boards_func(args,user):
	out=command.Command.json.copy()
	
	boards=database.query("SELECT * FROM boards WHERE hidden='0';")
	boardlist=""
	for i in boards:
		boardlist+="<br> {"+i['id']+"} | "+i['name']
	
	out.update({
		"DisplayItems":[
			display.Item("Retrieving list of discussion boards"),
			display.Item(boardlist,donttype=True)
		],
		"ClearScreen":True
	})
	return out

command.Command("BOARDS","Displays list of available Discussion Boards",boards_func,10)