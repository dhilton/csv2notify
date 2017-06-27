# CSV to Notify

Stream a CSV file to GOV.UK Notify API


# Installation

If you don't use `pipsi`, you're missing out.
Here are [installation instructions](https://github.com/mitsuhiko/pipsi#readme).

Simply run:

    $ pipsi install .


# Usage

To use it:

    $ csv2notify --help

# Eh? Why?

For many UK Government departments, agencies, arms length bodies and local
authorities, you may want to use Notify now but for whatever reason can't make
use of the rest API interface nor use the web interface due to the volume of the
notifications you wish to send. This simple command line tool is designed to
solve this issue; you may be able to build a user centred frontend to your service
but the line of business system still runs as a [Open road](), [Cobal]() or a
vendor doesn't support a pluggable approach.

# To do

* Support partial failures of a run of a Notification session
* Flesh out the API design of the python cli
* Add support for unix pipe style input
* Review moving to golang, so that we can support multiple OS's with a single
binary install. Might make Windows and Solaris support for example v. easy if a
need is found for those platform supports.
* Merge in a cleaned up version of the `prototype-end-to-end-tracer` branch.
