<?php

namespace Services;

interface FSMInterface {

    /**
     * @param $orderId int
     * @param $status string
     * @param $event string
     * 
     * @return void
     */
    public function changeState(int $orderId, string $status, string $event): void;
    
    /**
     * @return string
     */
    public function getState(): string;
}