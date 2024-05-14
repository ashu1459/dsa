<?php

function autoloader($class) {
    $paths = [
        './',
        './Services/',
        './Services/Events/',
        './Services/Status/',
    ];

    foreach ($paths as $path) {
        $file = $path . $class . '.php';

        if (file_exists($file)) {
            include $file;
        }
    }   
}

spl_autoload_register('autoloader');

$orderService = new OrderService();

$fsm = $orderService->create();
$fsmUpdated = $orderService->changeState(1, 'RECEIVED', 'SHIP');
$fsmState = $orderService->getState(1);

echo "<pre>";
print_r($fsm);
var_dump($fsmUpdated);
print_r($fsmState);