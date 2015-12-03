
![yaaHN API](https://github.com/arindampradhan/yaaHN/blob/master/hn.png)

Yaa it's just a python wrapper for the official [firebase hacker news api](https://github.com/HackerNews/API).


## Install

    python setup.py install

    or 

    pip install yaaHN


## Features:

* No oauth required, use a simple client.
* Async requests (uses gevent) 
* Fetch comments, stories, poll, user data and lot more. 
* Comments easily support support pagination and comment kids.
* Hook them to your **django** and **flask** using models api.
* Easily initialize to your database from the api sql or nosql.
* Most objects have a simple schema for json and xml.

## **Client** for hacker New


### **``get_comments``**

#### Get all comment objects

#### Parameters:

Name | Type | Required | Description | Default
-----|------|----------|-------------|----------
item_id | int | Yes | The id of the item (story id or comment id) that has comments kid | None
limit      | int | No  | limit Number of comments to return | 5
json       | bool | No | If yes returns the json result     | False

#### Examples

    from yaaHN import hn_client
    hn_client.get_comments(6374031)

    [<Comment: ID=6375861>,
     <Comment: ID=6374318>,
     <Comment: ID=6376142>,
     <Comment: ID=6374429>,
     <Comment: ID=6374292>,
     <Comment: ID=6374678>,
     <Comment: ID=6374547>]

This method uses **gevent requests** 

### **``top_stories``**

#### Yields top 100 stories objects


#### Parameters:

Name  | Type | Required | Description | Default
------|------|----------|-------------|---------
limit | int | No | limit Number of comments to return | 5
first | int | No | set first range from top stories ids | None
last | int | No | set last range from top stories ids | None
json | bool | No | If yes returns the json result | False


#### Examples

This is a generator object

    from yaaHN import hn_client
    for r in hn_client.top_stories(30):
        print "%s  -  %s" %(r.id , r.title) 
        print 

This method uses **gevent requests**


### **``get_user``**

Returns an **User object**

    from yaaHN import hn_client
    hn_client.get_user('joe')

    <User: ID=joe>

### **``get_item``**

Returns an **Item object**

    from yaaHN import hn_client
    hn_client.get_item(1)

    <Item: ID=1>

**Note:** This item object accepts any type of item and can be used as a dummy object, for unrelaible exceptions due to async requests.(Usage in top_stories)

### **``get_poll``** , **``get_comment``**,**``get_story``** .

    from yaaHN import hn_client
    hn_client.get_item(8863)
    hn_client.get_story(879)
    hn_client.get_comment(2921983)

Poll, Story, Comment are subclass (not inherited) of item class . They all have some(not all) of the properties of the item class.

###  **``top_stories_ids``**

#### Returns the list of ids from top stories ( No parameter needed)

#### Examples

    from yaaHN import hn_client
    hn_client.top_stories_ids()

    [8976489,8976451,8976690,8976611,8974024,8973283, ... 

### **``get_max_item``**

Returns the **max item id**

#### Examples

    from yaaHN import hn_client
    hn_client.get_max_item()

###  **``updates``**

Get the **updates object**

#### Examples
    
    from yaaHN import hn_client
    hn_client.updates()

    items updated : 10

    a = hn_client.updates()

## **``models``** for yaaHN


##Tests

To run the tests locally

    $ ./run-tests.sh

To run individual test

    $ python -m unittest tests.<module name>

##Item

**properties**

Field | Description
------|------------
id | The item's unique id. Required.
deleted | `true` if the item is deleted.
type | The type of item. One of "job", "story", "comment", "poll", or "pollopt".
by | The username of the item's author.
time | Creation date of the item, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
text | The comment, Ask HN, or poll text. HTML.
dead | `true` if the item is dead.
parent | The item's parent. For comments, either another comment or the relevant story. For pollopts, the relevant poll.
kids | The ids of the item's comments, in ranked display order.
url | The URL of the story.
score | The story's score, or the votes for a pollopt.
title | The title of the story or poll.
parts | A list of related pollopts, in display order.

### ``Poll``, ``Comment`` , ``Story`` 

These are items themselves.(Not inherited but subclass )

##User

**properties**

Field | Description
------|------------
id | The user's unique username. Case-sensitive. Required.
delay | Delay in minutes between a comment's creation and its visibility to other users.
created | Creation date of the user, in [Unix Time](http://en.wikipedia.org/wiki/Unix_time).
karma | The user's karma.
about | The user's optional self-description. HTML.
submitted | List of the user's stories, polls and comments.


### **``types``**
* - **models.comment** - get the comment model
* - **models.item** - get the item model
* - **models.story** - get the story model
* - **models.user** - get the user model
* - **models.deleted** - get the deleted model 
* - **models.poll** - get the poll model
* - **models.update** - get the update model