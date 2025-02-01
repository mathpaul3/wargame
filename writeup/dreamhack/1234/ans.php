<?php
class Ticket {
    public $results;
    public $numbers;

    function issue() {
        $this->numbers = draw(45, 6);
    }
}

$ticket = new Ticket();
$ticket->results = array();
$ticket->numbers = &$ticket->results;
$data = serialize($ticket);
var_dump($data);
echo $data;
echo base64_encode($data);
?>