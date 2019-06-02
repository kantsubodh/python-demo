# coding=utf-8

#  Copyright (c) 2019. This project is created by @SubodhM

# 1 - imports
from datetime import date

from actor import Actor
from base import Session, engine, Base
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman

# 2 - generate database schema
Base.metadata.create_all(engine)

# 3 - create a new session
session = Session()

# 4 - create movies
bourne_identity = Movie(1, "The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie(2, "Furious 7", date(2015, 4, 2))
pain_and_gain = Movie(3, "Pain & Gain", date(2013, 8, 23))

# 5 - creates actors
matt_damon = Actor(1, "Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor(2, "Dwayne Johnson", date(1972, 5, 2))
mark_wahlberg = Actor(3, "Mark Wahlberg", date(1971, 6, 5))

# 6 - add actors to movies
bourne_identity.actors = [matt_damon]
furious_7.actors = [dwayne_johnson]
pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]

# 7 - add contact details to actors
matt_contact = ContactDetails(1,"415 555 2671", "Burbank, CA", matt_damon)
dwayne_contact = ContactDetails(2,"423 555 5623", "Glendale, CA", dwayne_johnson)
dwayne_contact_2 = ContactDetails(3,"421 444 2323", "West Hollywood, CA", dwayne_johnson)
mark_contact = ContactDetails(4,"421 333 9428", "Glendale, CA", mark_wahlberg)

# 8 - create stuntmen
matt_stuntman = Stuntman(1,"John Doe", True, matt_damon)
dwayne_stuntman = Stuntman(2,"John Roe", True, dwayne_johnson)
mark_stuntman = Stuntman(3,"Richard Roe", True, mark_wahlberg)

# 9 - persists data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)

session.add(matt_contact)
session.add(dwayne_contact)
session.add(dwayne_contact_2)
session.add(mark_contact)

session.add(matt_stuntman)
session.add(dwayne_stuntman)
session.add(mark_stuntman)

# 10 - commit and close session
session.commit()
session.close()