#!/usr/bin/perl
use strict;
use warnings;

# Input file
my $input_file = shift @ARGV or die "Usage: $0 input_file\n";

open(my $fh, "<", $input_file) or die "Cannot open file '$input_file': $!\n";

# Read header
my $header_line = <$fh>;
chomp $header_line;
my @headers = split(/\s/, $header_line);

# Check we have at least one population column
die "No population columns found.\n" if @headers < 2;

# Print new header with Assigned_Population
print join("\t", @headers, "Assigned_Population"), "\n";

# Process each sample
while (<$fh>) {
    chomp;
    my @fields = split(/\s/, $_);
    my $sample = $fields[0];
    my @q_values = @fields[1..$#fields];

    my $max_index = 0;
    my $max_value = $q_values[0];

    for my $i (1 .. $#q_values) {
        if ($q_values[$i] > $max_value) {
            $max_value = $q_values[$i];
            $max_index = $i;
        }
    }

    my $assigned_pop = $headers[$max_index + 1];  # +1 offset because sample is first column
    print join("\t", @fields, $assigned_pop), "\n";
}

close($fh);

=com

Input
Sample Pop1 Pop2 Pop3 Pop4 Pop5 Pop6 Pop7 Pop8 Pop9 Pop10
A01 0.033156 0.559335 0.000010 0.000010 0.023081 0.020323 0.000010 0.000010 0.300927 0.063138
A02 0.000010 0.000010 0.297797 0.100075 0.000013 0.000014 0.000010 0.055151 0.095193 0.451726
A03 0.076484 0.228335 0.000010 0.000010 0.006132 0.000010 0.000010 0.000010 0.688989 0.000010

Output
Sample	Pop1	Pop2	Pop3	Pop4	Pop5	Pop6	Pop7	Pop8	Pop9	Pop10	Assigned_Population
A01	0.033156	0.559335	0.000010	0.000010	0.023081	0.020323	0.000010	0.000010	0.300927	0.063138	Pop2
A02	0.000010	0.000010	0.297797	0.100075	0.000013	0.000014	0.000010	0.055151	0.095193	0.451726	Pop10
A03	0.076484	0.228335	0.000010	0.000010	0.006132	0.000010	0.000010	0.000010	0.688989	0.000010	Pop9
=cut

