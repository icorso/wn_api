"""


update user set password=md5('1'), passwordchangedate=CURDATE();
delete from password_reset_request;
"""