Action()
{

	web_url("login", 
		"URL=http://127.0.0.1:5000/user/login", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=", 
		"Snapshot=t1.inf", 
		"Mode=HTML", 
		LAST);

	web_submit_form("login_2", 
		"Snapshot=t2.inf", 
		ITEMDATA, 
		"Name=email", "Value=q030026117@mail.uic.edu.cn", ENDITEM, 
		"Name=password", "Value=qqqqqq", ENDITEM, 
		LAST);

	lr_think_time(25);

	lr_start_transaction("find_confirm_University");

	web_url("search", 
		"URL=http://127.0.0.1:5000/user/search", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:5000/user/userCase", 
		"Snapshot=t3.inf", 
		"Mode=HTML", 
		LAST);

	lr_think_time(8);

	web_submit_form("search_2",
		"Snapshot=t4.inf",
		ITEMDATA,
		"Name=select1", "Value=Search through GPA", ENDITEM,
		"Name=gpa", "Value={GPA}", ENDITEM,
		"Name=uname", "Value=something", ENDITEM,
		LAST);

	lr_end_transaction("find_confirm_University", LR_AUTO);

	lr_think_time(9);

	web_url("userCase", 
		"URL=http://127.0.0.1:5000/user/userCase", 
		"Resource=0", 
		"RecContentType=text/html", 
		"Referer=http://127.0.0.1:5000/user/search", 
		"Snapshot=t5.inf", 
		"Mode=HTML", 
		LAST);

	return 0;
}