import sys
import getopt
import mailbox

def main(argv):
	in_mbox = "allmail.mbox"
	prefix = "results/"
	try:
		opts, args = getopt.getopt(argv, "i:p:", ["infile=", "prefix="])
	except getopt.GetoptError:
		print("python splitgmail.py -i  -p ")
		sys.exit(2)

	for opt, arg in opts:
		if opt in ("-i", "--infile"):
			in_mbox = arg
		elif opt in ("-p", "--prefix"):
			prefix = arg
	print("Processing file - " +in_mbox+" with prefix = "+prefix)
	boxes = {"inbox": mailbox.mbox(prefix+"Inbox.mbox", None, True), "sent": mailbox.mbox(prefix+"Sent.mbox", None, True),"archive":mailbox.mbox(prefix+"Archive.mbox", None, True)}

	mnum=0
	for message in mailbox.mbox(in_mbox):
		mnum = mnum+1
		gmail_labels = message["X-Gmail-Labels"]       # Could possibly be None.
		if not gmail_labels:
			print(message)
			print("no gmail label, saving to ARCHIVE")
			print("===================")
			continue
		last_label = gmail_labels.split(',')[-1]
		slabel = str(last_label).replace('\r', '').replace('\n', '')
		print(slabel)
		print("---------------")

	print("")
	print("Number of messages was", mnum)
if __name__ == "__main__":
    main(sys.argv[1:])
