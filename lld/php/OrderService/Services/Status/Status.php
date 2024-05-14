<?php

use Services\Status\StatusConstants;
use Services\Status\StatusInterface;

Class Status implements StatusInterface {
    
    /**
     * @var string
     */
    private $status;

    /**
     * @return StatusInterface
     */
    public function __construct() {
        $this->status = StatusConstants::INIT;
    }

    /**
     * @return string
     */
    public function get(): string {
        return $this->status;
    }

    /**
     * @param string $status
     * 
     * @return void
     */
    public function set($status): void {
        $this->status = $status;
    }

    /**
     * @param string $status
     * 
     * @return string|null
     */
    public function getText($status): string|null {

        if (StatusConstants::statusExists($status)) {
            return $status;
        }

        return null;
    }
}